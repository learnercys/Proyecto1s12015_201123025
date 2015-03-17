/**
 * Created by learnercys on 3/16/15.
 */
"use strict";

(function (angular) {
    angular.module('usersSystem')
        .service('Auth', [
            '$cookieStore',
            'Restangular',
            function (
                $cookieStore,
                Restangular
            ) {
                var
                    self = this,
                    token = null;

                self.getToken = function () {
                    var _token = token ? token : $cookieStore.get('token');

                    return angular.isUndefined( _token ) ? false: _token;
                };
                
                self.login = function (data, success, fail, end) {
                    Restangular
                        .all('login')
                        .post(data)
                        .then( function ( response ) {

                            if( angular.isFunction(success) ) {
                                success(response);
                            }

                            self.setToken(response.token);

                        }, function ( error ) {
                            if( angular.isFunction( fail) ) {
                                fail(error.data);
                            }
                        })
                        .finally( function ( ) {
                            if( angular.isFunction( end ) ) {
                                end();
                            }
                        });
                };

                self.register = function( data, success, fail, end ) {
                  Restangular
                      .all('users')
                      .all('create')
                      .post(data)
                      .then( function ( response ) {
                          if( angular.isFunction( success ) ) {
                              success( response );
                          }
                      }, function ( error ) {
                          if( angular.isFunction( fail ) ) {
                              fail( error.data );
                          }
                      }).finally( function ( ) {
                          if ( angular.isFunction( end ) ) {
                              end();
                          }
                      });
                };

                self.setToken = function (_token) {
                    $cookieStore.put('token', _token);
                    token = _token;
                }

                
            } 
        ]);
})(window.angular);
