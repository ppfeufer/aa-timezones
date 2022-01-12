/* global moment, aaTimezonesPanels, aaTimezonesOptions */

'use strict';

let clockTarget = 0;
let clockTickId = 0;
let countdownIntervalId = 0;

/**
 * Show the time adjust section
 */
function showAdjust () {
    jQuery('#btnadjust').addClass('hidden');
    jQuery('#adjust').removeClass('hidden');

    const mom = moment.tz(new Date(), 'Etc/UTC');

    jQuery('#tathour').val(mom.format('HH'));
    jQuery('#tatminute').val(mom.format('mm'));
    jQuery('#tatday').val(mom.format('DD'));
    jQuery('#tatmonth').val(mom.format('MM'));
    jQuery('#tatyear').val(mom.format('YYYY'));
}

/**
 * Set time for in x day, y hours, z minutes
 */
function reloadToTimestamp () {
    const timestamp = (
        (new Date).getTime() / 1000
        + jQuery('#tind').val() * 24 * 60 * 60
        + jQuery('#tinh').val() * 60 * 60
        + jQuery('#tinm').val() * 60
    );

    window.location.replace(aaTimezonesOptions.base_url + timestamp);
}

/**
 * Reload to base page
 */
function reloadBasePage () {
    window.location.replace(aaTimezonesOptions.base_url);
}

/**
 * Set the date
 *
 * @param str
 * @param tz
 */
function setdate (str, tz) {
    if (tz !== '') {
        window.location.replace(
            aaTimezonesOptions.base_url + moment.tz(str, tz).unix()
        );
    } else {
        window.location.replace(
            aaTimezonesOptions.base_url + moment(str).unix()
        );
    }
}

/**
 * Update the timezone panel
 *
 * @param mom
 * @param id
 */
function updatePanel (mom, id) {
    jQuery('#time-' + id).html(mom.format('HH:mm:ss'));
    jQuery('#utc-offset-' + id).html('(UTC ' + mom.format('Z') + ')');
    jQuery('#date-' + id).html(mom.format('dddd DD MMM YYYY'));

    /**
     * Update the weather icon
     *    3 06-09 sunrise
     *    3 09-11 sun
     *    3 11-14 sun
     *    3 14-17 sun
     *    3 17-20 sunset
     *    3 20-23 moonrise
     *    4 23-03 moon
     *    3 03-06 moonset
     */
    const h = mom.format('H') * 1;
    let icon = 'wi wi-night-clear';

    if (h < 23) {
        icon = 'wi wi-moonrise';
    }

    if (h < 20) {
        icon = 'wi wi-sunset';
    }

    if (h < 17) {
        icon = 'wi wi-day-sunny';
    }

    if (h < 14) {
        icon = 'wi wi-day-sunny';
    }

    if (h < 11) {
        icon = 'wi wi-day-sunny';
    }

    if (h < 9) {
        icon = 'wi wi-sunrise';
    }

    if (h < 6) {
        icon = 'wi wi-moonset';
    }

    if (h < 3) {
        icon = 'wi wi-night-clear';
    }

    // Set the icon
    jQuery('#icon-' + id).removeClass().addClass(icon);
}

/**
 * Bulk update the timezone panels
 *
 * @param now
 */
function updatePanels (now) {
    // local time
    updatePanel(moment(now), 'local-time');

    // panels
    jQuery.each(aaTimezonesPanels, function (index, value) {
        updatePanel(moment.tz(now, value.timezoneName), value.timezoneId);
    });
}

/**
 * Time until given timestamp
 * @param timestamp
 */
function timeUntil (timestamp) {
    const timestampDifference = timestamp - Date.now();
    let timeDifferenceInSeconds = timestampDifference / 1000; // from ms to seconds

    // set the interval
    countdownIntervalId = setInterval(function () { // execute code each second
        let countdown;

        timeDifferenceInSeconds--; // decrement timestamp with one second each second

        if (timeDifferenceInSeconds >= 0) {
            const days = Math.floor(timeDifferenceInSeconds / (24 * 60 * 60)); // calculate days from timestamp
            let hours = Math.floor(timeDifferenceInSeconds / (60 * 60)) % 24; // hours
            let minutes = Math.floor(timeDifferenceInSeconds / 60) % 60; // minutes
            let seconds = Math.floor(timeDifferenceInSeconds) % 60; // seconds

            // leading zero ...
            if (hours < 10) {
                hours = '0' + hours;
            }
            if (minutes < 10) {
                minutes = '0' + minutes;
            }
            if (seconds < 10) {
                seconds = '0' + seconds;
            }

            countdown = days + ' ' + aaTimezonesOptions.translation.days + ', ' + hours + ':' + minutes + ':' + seconds;
        } else {
            countdown = aaTimezonesOptions.translation.alreadyOver;
        }

        $('.aa-timezones-time-until-countdown').html(countdown);
    }, 1000);
}

/**
 * Callback to set the clock interval
 *
 * @see switchto()
 */
function clockTick () {
    updatePanels(new Date());
}

/**
 * Switch between time-adh´just mode and normal view mode
 *
 * @param mode
 */
function switchto (mode) {
    if (clockTickId !== 0) {
        clearInterval(clockTickId);
    }

    if (countdownIntervalId !== 0) {
        clearInterval(countdownIntervalId);
    }

    $('.aa-timezones-time-until-countdown').html('');

    if (mode === 0) {
        jQuery('#headlineCurrent').removeClass('hidden');
        jQuery('#headlineFixed').addClass('hidden');
        jQuery('#adjust').addClass('hidden');
        jQuery('#btnadjust').removeClass('hidden');
        jQuery('#btnshowcurrent').addClass('hidden');
        jQuery('.aa-timezones-time-until').addClass('hidden');

        if (clockTarget !== 0) {
            jQuery('#btnshowfixed').removeClass('hidden');
        }

        jQuery('#btnclear').addClass('hidden');

        clockTickId = setInterval(clockTick, 1000);

        clockTick();
    } else {
        jQuery('#headlineCurrent').addClass('hidden');
        jQuery('#headlineFixed').removeClass('hidden');
        jQuery('#adjust').addClass('hidden');
        jQuery('#btnadjust').addClass('hidden');
        jQuery('#btnshowcurrent').removeClass('hidden');
        jQuery('#btnshowfixed').addClass('hidden');
        jQuery('#btnclear').removeClass('hidden');
        jQuery('.aa-timezones-time-until').removeClass('hidden');

        updatePanels(new Date(clockTarget));
        timeUntil(clockTarget);
    }
}

/**
 * Timestamp has changed
 */
function hashchange () {
    const ts = parseInt(aaTimezonesOptions.timestamp);

    clockTarget = 0;

    if (!isNaN(ts) && isFinite(ts)) {
        clockTarget = ts * 1000;

        const mom = moment.tz(new Date(clockTarget), 'Etc/UTC');

        jQuery('#timestamp').attr(
            'datetime', mom.format('YYYY-MM-DDTHH:mm:00Z0000')
        ).timeago('update', new Date(clockTarget));
    }

    switchto(clockTarget);
}

jQuery(document).ready(function ($) {
    window.addEventListener('hashchange', hashchange, false);

    /**
     * Declaring some variables ...
     */
    const mom = moment.tz(new Date(), 'Etc/UTC');
    const year = mom.format('YYYY') * 1;
    let i;

    for (i = year - 4; i < year + 5; i++) {
        $('#tatyear').append($('<option>', {i: i}).text(i));
    }

    $.timeago.settings.allowFuture = true;
    $.timeago.settings.allowPast = true;

    setInterval(function () {
        $('#timestamp').timeago('update', new Date(clockTarget));
    }, 10000);

    hashchange();
});
