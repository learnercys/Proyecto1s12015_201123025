/**
 * Created by learnerc on 3/6/15.
 */

"use strict";

angular.module('usersSystem', [
    'ngCookies',
    'restangular'
]).config([
    'RestangularProvider',
    function (
        RestangularProvider
    ) {
        var
            url = 'http://localhost:9090',
            services = '/api';


        // config restangular
        RestangularProvider.setBaseUrl(url + services);

        RestangularProvider.setDefaultHeaders({
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        })
    }
]);

