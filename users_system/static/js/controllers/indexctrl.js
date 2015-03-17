/**
 * Created by learnercys on 3/17/15.
 */

angular.module('usersSystem').controller('IndexCtrl',
    function (
        $scope
    ) {
        $scope.options = {
            showDeleteAccount: false
        };
        $scope.deleteAccount = function () {

        };
    }
);

