/* global moment, aaTimezonesPanels, aaTimezonesOptions */

let clockTarget = 0;
let clockTickId = 0;
let countdownIntervalId = 0;

/**
 * Show the "time adjust" section
 */
const showAdjust = () => { // eslint-disable-line no-unused-vars
    'use strict';

    jQuery('#btnadjust').addClass('d-none');
    jQuery('#adjust').removeClass('d-none');

    const mom = moment.tz(new Date(), 'Etc/UTC');

    jQuery('#tathour').val(mom.format('HH'));
    jQuery('#tatminute').val(mom.format('mm'));
    jQuery('#tatday').val(mom.format('DD'));
    jQuery('#tatmonth').val(mom.format('MM'));
    jQuery('#tatyear').val(mom.format('YYYY'));
};

/**
 * Reload to given location
 *
 * @param {string} location The location to reload to
 */
const reloadToLocation = (location) => {
    'use strict';

    window.location.replace(location);
};

/**
 * Reload to base page
 */
const reloadBasePage = () => { // eslint-disable-line no-unused-vars
    'use strict';

    reloadToLocation(aaTimezonesOptions.base_url);
};

/**
 * Set time for in x days, y hours, z minutes
 *
 * @param {int} days Number of days
 * @param {int} hours Number of hours
 * @param {int} minutes Number of minutes
 */
const setTimeToBeIn = (days, hours, minutes) => { // eslint-disable-line no-unused-vars
    'use strict';

    // const timestamp = (
    //     new Date()
    //         .getTime() / 1000 + jQuery('#tind')
    //         .val() * 24 * 60 * 60 + jQuery('#tinh')
    //         .val() * 60 * 60 + jQuery('#tinm')
    //         .val() * 60
    // );

    const timestamp = moment().unix() + days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60;

    reloadToLocation(aaTimezonesOptions.base_url + timestamp);
};

/**
 * Set the date, time and time zone
 *
 * @param {string} datetime
 * @param {string} timezone
 */
const setDateAndTime = (datetime, timezone) => { // eslint-disable-line no-unused-vars
    'use strict';

    if (timezone !== '') {
        reloadToLocation(
            aaTimezonesOptions.base_url + moment.tz(datetime, timezone).unix()
        );
    } else {
        reloadToLocation(
            aaTimezonesOptions.base_url + moment(datetime).unix()
        );
    }
};

/**
 * Update the timezone panel
 *
 * @param mom
 * @param id
 */
const updatePanel = (mom, id) => {
    'use strict';

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
};

/**
 * Bulk update the timezone panels
 *
 * @param {Date} now
 */
const updatePanels = (now) => {
    'use strict';

    // local time
    updatePanel(moment(now), 'local-time');

    // panels
    jQuery.each(aaTimezonesPanels, function (index, value) {
        updatePanel(moment.tz(now, value.timezoneName), value.timezoneId);
    });
};

/**
 * Time until given timestamp
 *
 * @param {number} timestamp
 */
const timeUntil = (timestamp) => {
    'use strict';

    /**
     * Update the countdown
     */
    const updateCountdown = () => {
        const now = Date.now();
        const timestampDifference = timestamp - now;
        let timeDifferenceInSeconds = timestampDifference / 1000; // from ms to seconds

        let countdown;

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

        // Calculate drift and set the next interval
        const drift = 1000 - (Date.now() - now);

        countdownIntervalId = setTimeout(
            updateCountdown,
            Math.max(0, drift)
        );
    };

    updateCountdown();
};

/**
 * Callback to set the clock interval
 *
 * @see switchto()
 */
const clockTick = () => {
    'use strict';

    updatePanels(new Date());
};

/**
 * Switch between time-adh´just mode and normal view mode
 *
 * @param {int} mode
 */
const switchto = (mode) => {
    'use strict';

    if (clockTickId !== 0) {
        clearInterval(clockTickId);
    }

    if (countdownIntervalId !== 0) {
        clearInterval(countdownIntervalId);
    }

    $('.aa-timezones-time-until-countdown').html('');

    if (mode === 0) {
        jQuery('#headlineCurrent').removeClass('d-none');
        jQuery('#headlineFixed').addClass('d-none');
        jQuery('#adjust').addClass('d-none');
        jQuery('#btnadjust').removeClass('d-none');
        jQuery('#btnshowcurrent').addClass('d-none');
        jQuery('.aa-timezones-time-until').addClass('d-none');

        if (clockTarget !== 0) {
            jQuery('#btnshowfixed').removeClass('d-none');
        }

        jQuery('#btnclear').addClass('d-none');

        clockTickId = setInterval(clockTick, 1000);

        clockTick();
    } else {
        jQuery('#headlineCurrent').addClass('d-none');
        jQuery('#headlineFixed').removeClass('d-none');
        jQuery('#adjust').addClass('d-none');
        jQuery('#btnadjust').addClass('d-none');
        jQuery('#btnshowcurrent').removeClass('d-none');
        jQuery('#btnshowfixed').addClass('d-none');
        jQuery('#btnclear').removeClass('d-none');
        jQuery('.aa-timezones-time-until').removeClass('d-none');

        updatePanels(new Date(clockTarget));
        timeUntil(clockTarget);
    }
};

/**
 * Timestamp has changed
 */
const hashchange = () => {
    'use strict';

    const timestamp = parseInt(aaTimezonesOptions.timestamp);

    clockTarget = 0;

    if (!isNaN(timestamp) && isFinite(timestamp)) {
        clockTarget = timestamp * 1000;

        const mom = moment.tz(new Date(clockTarget), 'Etc/UTC');

        jQuery('#timestamp').attr(
            'datetime', mom.format('YYYY-MM-DDTHH:mm:00Z0000')
        ).timeago('update', new Date(clockTarget));
    }

    switchto(clockTarget);
};

jQuery(document).ready(($) => {
    'use strict';

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

    setInterval(() => {
        $('#timestamp').timeago('update', new Date(clockTarget));
    }, 10000);

    hashchange();
});
