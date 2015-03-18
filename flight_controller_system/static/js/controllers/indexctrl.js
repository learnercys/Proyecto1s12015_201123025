/**
 * Created by carlos on 17/03/15.
 */

angular.module('flightControllerSystem').controller('IndexCtrl',
    function (
        $scope,
        $timeout,
        Airport
    ) {
        $scope.options = {
            page: 'index'
        };

        $scope.createAirport = function () {
            Airport.create({
                name: $scope.airportName,
                actualCountry: $scope.airportActualCountry,
                password: $scope.airportPassword

            }, function ( /*response */ ) {
                $timeout(function ( ) {
                    $scope.options.page = 'index';
                }, 200)
            }, function ( error ) {

            }, function ( ) {

            });
        };

        $scope.deleteAccount = function () {

        };
    }
);
