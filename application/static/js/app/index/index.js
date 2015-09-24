/**
 * Created by lkz on 2015/09/24 14:54.
 */

define(function(require, exports){
    var $ = require('jquery');
    var _ = require('backbone');

    var timeTpl = _.template(
                  "<div class='step-clock'>" +
                     "<span class='date'><%- month %>/<%-day%></span>" +
                     "<span class='time><%- [hour, minute, seconds].join(':') %></span>" +
                  "</div>");

    exports.formatTime = function (date) {
        var time = {
            month:  date.getMonth(),
            day: date.getDate(),
            hour: date.getHours(),
            minute: date.getMinutes(),
            seconds: date.getSeconds()
        };

        return timeTpl(time);
    };

    exports.init = function (selector) {
        var $target = typeof selector === 'string' ? $(selector) : selector;

        setInterval(function (){
            $target.html(exports.formatTime(new Date));
        }, 1000)
    };
});