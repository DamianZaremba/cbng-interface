(function () {
    'use strict';

    // TODO - Angularify?
    var reportCtrl = function ($scope, $rootScope, $http) {
        $scope.change_status = function(revert_id, status_id) {
            $http.get('/cluebotng/report/' + revert_id + '/status/' + status_id)
                .then(function(response){
                    if(response.data.status == 'OK') {
                        $('#status').text(response.data.report_status);
                        if(response.data.next) {
                           window.location = '/cluebotng/report/' + response.data.next;
                        }
                    }
                });
        };

        //$scope.delete_comment = function(comment_id) {
        //    $http.delete('/cluebotng/report/api/v1/comments/' + comment_id + '/')
        //        .then(function(response){
        //            console.log(response);
        //        });
        //    $("#comment-" + comment_id).remove();
        //};
    };
    reportCtrl.$inject = ['$scope', '$rootScope', '$http'];

    angular.module('cbngApp').controller('ReportCtrl', reportCtrl);
}());