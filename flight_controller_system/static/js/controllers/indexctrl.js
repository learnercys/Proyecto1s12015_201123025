/**
 * Created by carlos on 17/03/15.
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
