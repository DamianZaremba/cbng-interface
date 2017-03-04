(function () {
    'use strict';

    var reviewCtrl = function ($scope, $rootScope, $http, $sce) {
        $scope.get_next = function() {
            $('#confirm').hide();
            $('#comments').val('');
            $http.get('/cluebotng/review/japi/next/')
                .then(function(response) {
                        if(response.data.status == 'OK') {
                            $scope.edit = {
                                'id': response.data.id,
                                'diff': $sce.trustAsHtml(response.data.diff),
                                'article': response.data.article,
                                'force': false
                            };
                        } else {
                            $scope.error = response.data.error;
                        }
                    }, function(response) {
                        $scope.error = 'API error: ' + response.status;
                    }
                );
        };

        $scope.score_edit = function(score) {
            $('#confirm').hide();
            if($scope.edit && $scope.edit.id) {
                $http.get('/cluebotng/review/japi/score/' +
                            encodeURI($scope.edit.id) + '/' +
                            encodeURI(score) + '?force=' +
                            encodeURI($scope.edit.force) +
                            '&comment=' + encodeURI($('#comments').val()))
                    .then(function(response){
                        if(response.data.status == 'OK') {
                            if(response.data.confirm) {
                                $scope.error = 'Are you sure?';
                                $scope.edit.force = true;
                            } else {
                                $scope.get_next();
                            }
                        } else {
                            $scope.error = 'Unknown error';
                        }
                    }, function(response) {
                            $scope.error = 'API error: ' + response.status;
                    });
            }
        };

        $scope.get_next();
    };
    reviewCtrl.$inject = ['$scope', '$rootScope', '$http', '$sce'];

    angular.module('cbngApp').controller('ReviewCtrl', reviewCtrl);
}());