/* global moment, aaTimezonesPanels, aaTimezonesOptions, aaTimezonesTranslations, aaTimezonesAdjustOptions */

var clockTarget = 0;
var clockTickId = 0;
var countdownIntervalId = 0;

function showAdjust() {
    jQuery('#btnadjust').addClass('hidden');
    jQuery('#adjust').removeClass('hidden');

    var mom = moment.tz(new Date(), 'Etc/UTC');

    jQuery('#tathour').val(mom.format('HH'));
    jQuery('#tatminute').val(mom.format('mm'));
    jQuery('#tatday').val(mom.format('DD'));
    jQuery('#tatmonth').val(mom.format('MM'));
    jQuery('#tatyear').val(mom.format('YYYY'));
}

// set time for in x day, y hours, z minutes
function reloadToTimestamp() {
    var timestamp = parseInt(new Date().getTime() / 1000) + jQuery('#tind').val() * 24 * 60 * 60 + jQuery('#tinh').val() * 60 * 60 + jQuery('#tinm').val() * 60;

    window.location.replace(aaTimezonesOptions.base_url + timestamp);
}

// reload to base page
function reloadBasePage() {
    window.location.replace(aaTimezonesOptions.base_url);
}

function setdate(str, tz) {
    if(tz !== '') {
        window.location.replace(aaTimezonesOptions.base_url + moment.tz(str, tz).unix());
    } else {
        window.location.replace(aaTimezonesOptions.base_url + moment(str).unix());
    }
}

function updatePanel(mom, id) {
    jQuery('#time-' + id).html(mom.format('HH:mm:ss'));
    jQuery('#utc-offset-' + id).html('(UTC ' + mom.format('Z') + ')');
    jQuery('#date-' + id).html(mom.format('dddd DD MMM YYYY'));

//    3 06-09 sunrise
//    3 09-11 sun
//    3 11-14 sun
//    3 14-17 sun
//    3 17-20 sunset
//    3 20-23 moonrise
//    4 23-03 moon
//    3 03-06 moonset
    jQuery('#icon-' + id).removeClass();

    var h = mom.format('H') * 1;
    var icon = 'wi wi-night-clear';

    if(h < 23) {
        icon = 'wi wi-moonrise';
    }

    if(h < 20) {
        icon = 'wi wi-sunset';
    }

    if(h < 17) {
        icon = 'wi wi-day-sunny';
    }

    if(h < 14) {
        icon = 'wi wi-day-sunny';
    }

    if(h < 11) {
        icon = 'wi wi-day-sunny';
    }

    if(h < 9) {
        icon = 'wi wi-sunrise';
    }

    if(h < 6) {
        icon = 'wi wi-moonset';
    }

    if(h < 3) {
        icon = 'wi wi-night-clear';
    }

    jQuery('#icon-' + id).addClass(icon);
}

function updatePanels(now) {
    // local time
    updatePanel(moment(now), 'local-time');

    // panels
    jQuery.each(aaTimezonesPanels, function(index, value) {
        updatePanel(moment.tz(now, value.timezoneName), value.timezoneId);
    });
}

function timeUntil(timestamp) {
    var timestampDifference = timestamp - Date.now();
    var timeDifferenceInSeconds = timestampDifference / 1000; // from ms to seconds

    // set the interval
    countdownIntervalId = setInterval(function() { // execute code each second
        timeDifferenceInSeconds--; // decrement timestamp with one second each second

        if(timeDifferenceInSeconds >= 0) {
            var days    = Math.floor(timeDifferenceInSeconds / (24 * 60 * 60)); // calculate days from timestamp
            var hours   = Math.floor(timeDifferenceInSeconds / (60 * 60)) % 24; // hours
            var minutes = Math.floor(timeDifferenceInSeconds / 60) % 60; // minutes
            var seconds = Math.floor(timeDifferenceInSeconds / 1) % 60; // seconds

            // leading zero ...
            if(hours < 10) {hours = '0' + hours;}
            if(minutes < 10) {minutes = '0' + minutes;}
            if(seconds < 10) {seconds = '0' + seconds;}

            var countdown = days + ' ' + aaTimezonesTranslations.days + ', ' + hours + ':' + minutes + ':' + seconds;
        } else {
            var countdown = aaTimezonesTranslations.alreadyOver;
        }

        $('.aa-timezones-time-until-countdown').html(countdown);
    }, 1000);
}

function clockTick() {
    updatePanels(new Date());
}

function switchto(mode) {
    if(clockTickId !== 0) {
        clearInterval(clockTickId);
    }

    if(countdownIntervalId !== 0) {
        clearInterval(countdownIntervalId);
    }

    $('.aa-timezones-time-until-countdown').html('');

    if(mode === 0) {
        jQuery('#headlineCurrent').removeClass('hidden');
        jQuery('#headlineFixed').addClass('hidden');
        jQuery('#adjust').addClass('hidden');
        jQuery('#btnadjust').removeClass('hidden');
        jQuery('#btnshowcurrent').addClass('hidden');
        jQuery('.aa-timezones-time-until').addClass('hidden');

        if(clockTarget !== 0) {
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

function hashchange() {
    var ts = aaTimezonesAdjustOptions.timestamp.substring(1);

    clockTarget = 0;

    if(!isNaN(parseFloat(ts)) && isFinite(ts)) {
        clockTarget = ts * 1000;

        var mom = moment.tz(new Date(clockTarget), 'Etc/UTC');

        jQuery('#timestamp').attr('datetime', mom.format('YYYY-MM-DDTHH:mm:00Z0000'));
        jQuery('#timestamp').timeago('update', new Date(clockTarget));
    }

    switchto(clockTarget);
}

jQuery(document).ready(function($) {
    window.addEventListener('hashchange', hashchange, false);

    /**
     * Declaring some variables ...
     */
    var mom = moment.tz(new Date(), 'Etc/UTC');
    var year = mom.format('YYYY') * 1;
    var i;

    for(i = year - 4; i < year + 5; i++) {
        $('#tatyear').append($('<option>', {i: i}).text(i));
    }

    $.timeago.settings.allowFuture = true;
    $.timeago.settings.allowPast = true;

    setInterval(function() {
        $('#timestamp').timeago('update', new Date(clockTarget));
    }, 10000);

    hashchange();
});
