/**
 * Created by carlos on 3/6/15.
 */

( function ( angular ) {
    angular.module('usersSystem').controller('LoginCtrl', function( $scope ) {
        $scope.submit = function () {
            console.log('submit');
        };
    });
})(window.angular);
