/**
 * Created by carlos on 3/6/15.
 */

( function ( angular ) {
    angular.module('usersSystem').controller('LoginCtrl', [
        '$scope',
        'Auth',
        function(
            $scope,
            Auth
        ) {
            $scope.submit = function () {
                Auth.login({
                    username: $scope.username,
                    password: $scope.password
                }, function ( response ) {

                }, function ( error ) {

                });
                console.log('submit');
            };
        }
    ]);
})(window.angular);
