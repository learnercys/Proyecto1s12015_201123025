/**
 * Created by carlos on 17/03/15.
 */

angular.module('flightControllerSystem')
    .service('Airport', function (
        Restangular
    ) {
        var
            self = this;

        self.create = function ( data, success, fail, end ) {
            Restangular
                .all('airports')
                .all('create')
                .post(data)
                .then( function ( response ) {
                    if ( angular.isFunction( success ) ) {
                        success( response );
                    }
                }, function ( error ) {
                    if( angular.isFunction( fail ) ) {
                        fail( error );
                    }
                }).finally( function ( ) {
                    if ( angular.isFunction( end ) ) {
                        end()
                    }
                });
        };
    });
