/**
 * Created by carlos on 3/6/15.
 */

( function ( angular ) {
    angular.module('usersSystem').controller('RegisterCtrl',
        function(
            $scope,
            $timeout,
            Auth

        ) {

            $scope.options = {
                message: '',
                danger: false,
                success: false
            };

            $scope.submit = function () {
                Auth.register({
                    username: $scope.username,
                    name: $scope.name,
                    password: $scope.password,
                    address: $scope.address,
                    phoneNumber: $scope.phoneNumber,
                    creditCardNumber: $scope.creditCardNumber,
                    actualAddress: $scope.actualAddress
                }, function ( response ) {
                    $scope.options.success = true;
                    if( response.message === 'user_created') {
                        $scope.options.message = 'User created. Redirecting...';
                    }
                    
                }, function ( error ) {
                    $scope.options.danger = true;
                    if( error.message === 'user_already_exist') {
                        $scope.options.message = 'User already exist';
                    }
                }, function ( ) {
                    $timeout( function () {
                        $scope.options.danger = false;

                        if( $scope.options.success ) {
                            document.location.href = 'login';
                        }

                        $scope.options.success = false;
                    }, 2000);
                });
            };
        }
    );
})(window.angular);
