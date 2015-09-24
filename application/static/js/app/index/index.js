/**
 * Created by lkz on 2015/09/24 14:54.
 */

define(function(require, exports){
    var $ = require('jquery');
    var _ = require('underscore');

    var timeTpl = _.template(require('text!./templates/time.tpl'));

    exports.formatTime = function (date) {
        var time = {
            month:  date.getMonth(),
            day: date.getDate(),
            hours: date.getHours(),
            minutes: date.getMinutes(),
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