/**
 * Created by learnercys on 3/16/15.
 */

"use strict";

angular.module('usersSystem').run([
    'Auth',
    function (
        Auth
    ) {

        var location = window.location.href.substr(window.location.href.lastIndexOf('/') + 1, window.location.href.length);

        if( !Auth.getToken()  ) {

            if( location !== 'login' && location !== 'register') {
                window.location.href = 'login'
            }

        } else {
            if( location === 'login' || location === 'register' ) {
                window.location.href = '/';
            }
        }
    }
]);


