/**
 * Created by carlos on 3/6/15.
 */


angular.module('usersSystem').controller('LoginCtrl', [
    '$scope',
    '$timeout',
    'Auth',
    function(
        $scope,
        $timeout,
        Auth
    ) {
        $scope.options = {
            message: '',
            type: false
        };

        $scope.submit = function () {

            Auth.login({
                username: $scope.username,
                password: $scope.password
            }, function (  ) {
                $scope.options.message = 'Logged. Redirecting';
                $scope.options.type = 'success';
                $timeout( function ( ) {
                    document.location.href = '/';
                }, 2000)
            }, function ( error ) {
                $scope.options.message = 'Username y/o password does not match';
                $scope.options.type = 'danger';
            }, function ( ) {
                $timeout(function ( ) {
                    $scope.options.type = false;
                }, 2000);
            });
        };
    }
]);

