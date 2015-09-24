//The build will inline common dependencies into this file.

//For any third party dependencies, like jQuery, place them in the lib folder.

//Configure loading modules from the lib directory,
//except for 'app' ones, which are in a sibling
//directory.

requirejs.config({
    baseUrl: '/static/js/bower_components',
    paths: {
        app: '../app',
        jquery: 'jquery/dist/jquery.min',
        underscore: 'underscore/underscore',
        backbone: 'backbone/backbone',
        bootstrap: 'bootstrap/dist/js/bootstrap.min',
        cookie: 'cookie/src/cookie'
    },

    shim: {
        underscore: {
            exports: '_'
        },

        backbone: {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        },

        'bootstrap': {
            deps: ["jquery"]
        }
    }
});
