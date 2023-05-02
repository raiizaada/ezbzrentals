/*
Template Name: Nazox -  Admin & Dashboard Template
Author: Themesdesign
Contact: themesdesign.in@gmail.com
File: Calendar
*/

!function($) {
    "use strict";

    var CalendarPage = function() {};

    mobiscroll.setOptions({ 
        locale: mobiscroll.localeEn,        // Specify language like: locale: mobiscroll.localePl or omit setting to use default
        theme: 'windows',                   // Specify theme like: theme: 'ios' or omit setting to use default
            themeVariant: 'light'           // More info about themeVariant: https://docs.mobiscroll.com/5-19-2/eventcalendar#opt-themeVariant
    });
    
    var now = new Date();
    var day = now.getDay();
    var monday = now.getDate() - day + (day == 0 ? -6 : 1);
    //var rentalUrl = 'http://127.0.0.1:8000/api/rentals/';

    var getRental = $.getJSON('http://127.0.0.1:8000/api/rentals/', function(data){
        //console.log(data);
        var jsonRental = jQuery.parseJSON(data);
        console.log(jsonRental);
    });
    //var json = jQuery.parseJSON(getRental);
   
    CalendarPage.prototype.init = function() {


        $(function () {
    
            var inst = $('#calendar').mobiscroll().eventcalendar({
                
                view: {                   // More info about view: https://docs.mobiscroll.com/5-19-2/eventcalendar#opt-view
                    timeline: {
                        type: 'month'
                    }
                },
                resources: [{             // More info about resources: https://docs.mobiscroll.com/5-19-2/eventcalendar#opt-resources
                    id: 1,
                    name: 'Resource 1',
                    color: '#fdf500'
                }, {
                    id: 2,
                    name: 'Resource 2',
                    color: '#ff4600'
                }, {
                    id: 3,
                    name: 'Resource 3',
                    color: '#ff0101'
                }, {
                    id: 4,
                    name: 'Resource 4',
                    color: '#239a21'
                }, {
                    id: 5,
                    name: 'Resource 5',
                    color: '#8f1ed6'
                }, {
                    id: 6,
                    name: 'Resource 6',
                    color: '#01adff'
                }],
                data: [{                  // More info about data: https://docs.mobiscroll.com/5-19-2/eventcalendar#opt-data
                    id: 1,
                    start: '2022-11-01T00:00',
                    end: '2022-11-14T00:00',
                    title: 'Event 1',
                    resource: 1
                }, {
                    id: 2,
                    start: '2022-11-03T00:00',
                    end: '2022-11-05T00:00',
                    title: 'Event 2',
                    resource: 1
                }, {
                    id: 3,
                    start: '2022-11-06T00:00',
                    end: '2022-11-08T00:00',
                    title: 'Event 3',
                    resource: 2
                }, {
                    id: 4,
                    start: '2022-11-06T00:00',
                    end: '2022-11-09T00:00',
                    title: 'Event 4',
                    resource: 2
                }, {
                    id: 5,
                    start: '2022-11-09T00:00',
                    end: '2022-11-11T00:00',
                    title: 'Event 5',
                    resource: 3
                }, {
                    id: 6,
                    start: '2022-11-10T00:00',
                    end: '2022-11-12T00:00',
                    title: 'Event 6',
                    resource: 3
                }, {
                    id: 7,
                    start: '2022-11-13T00:00',
                    end: '2022-11-30T00:00',
                    title: 'Event 7',
                    resource: 4
                }, {
                    id: 8,
                    start: '2022-11-14T00:00',
                    end: '2022-11-17T00:00',
                    title: 'Event 8',
                    resource: 4
                }, {
                    id: 9,
                    start: '2022-11-18T00:00',
                    end: '2022-11-20T00:00',
                    title: 'Event 9',
                    resource: 5
                }, {
                    id: 10,
                    start: '2022-11-19T00:00',
                    end: '2022-11-22T00:00',
                    title: 'Event 10',
                    resource: 5
                }, {
                    id: 11,
                    start: '2022-11-22T00:00',
                    end: '2022-11-26T00:00',
                    title: 'Event 11',
                    resource: 6
                }, {
                    id: 12,
                    start: '2022-11-24T00:00',
                    end: '2022-11-28T00:00',
                    title: 'Event 12',
                    resource: 6
                }]
              
            });
        });

    },
    //init
    $.CalendarPage = new CalendarPage, $.CalendarPage.Constructor = CalendarPage
}(window.jQuery),

//initializing 
function($) {
    "use strict";
    $.CalendarPage.init()
}(window.jQuery);