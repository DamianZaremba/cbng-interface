(function () {
    'use strict';

    // TODO - Angularify?
    var reportCtrl = function ($scope, $rootScope, $http) {
        $scope.change_status = function(revert_id, status_id) {
            $http.get('/report/' + revert_id + '/status/' + status_id)
                .then(function(response){
                    if(response.data.status == 'OK') {
                        $('#status').text(response.data.report_status);
                        if(response.data.next_report) {
                           window.location = '/report/' + response.data.next_report;
                        }
                    }
                });
        };
    };
    reportCtrl.$inject = ['$scope', '$rootScope', '$http'];

    angular.module('cbngApp').controller('ReportCtrl', reportCtrl);
}());