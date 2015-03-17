/**
 * Created by carlos on 17/03/15.
 */

"use strict";

angular.module('flightControllerSystem', [
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
        });
    }
]);
