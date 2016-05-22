(function () {
    'use strict';

    var cbngApp = angular.module(
        'cbngApp',
        [
            'ui.bootstrap',
            'angular-loading-bar'
        ]
    );

    var loadingBarConfig = function (cfpLoadingBarProvider) {
        cfpLoadingBarProvider.latencyThreshold = 100;
        cfpLoadingBarProvider.includeSpinner = false;
        cfpLoadingBarProvider.includeBar = true;
    };
    loadingBarConfig.$inject = ['cfpLoadingBarProvider'];
    cbngApp.config(loadingBarConfig);

    var logProvider = function ($logProvider, devMode) {
        $logProvider.debugEnabled(devMode);
    };
    logProvider.$inject = ['$logProvider', 'devMode'];
    cbngApp.config(logProvider);
}());