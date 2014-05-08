/**
 * Created by jcaine on 5/7/14.
 */

google.load('visualization', '1.0', {'packages':['corechart']});
google.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the line chart, passes in the data and
// draws it.
function drawChart() {

    // json for table data
    var jsonData = {
        cols: [
            {id: 'date', label: 'Sample Date', type: 'date'},
            {id: 'countervalue', label: 'Counter Value', type: 'number'}
        ],

        rows: [
            {c: [ {v: new Date(2014, 4, 30, 10, 30, 0)}, {v: 2457.0} ] },
            {c: [ {v: new Date(2014, 4, 30, 10, 30, 15)}, {v: 2458.0} ] },
            {c: [ {v: new Date(2014, 4, 30, 10, 30, 30)}, {v: 2459.0} ] },
            {c: [ {v: new Date(2014, 4, 30, 10, 30, 45)}, {v: 2452.0} ] },
            {c: [ {v: new Date(2014, 4, 30, 10, 31, 0)}, {v: 2451.0} ] },
            {c: [ {v: new Date(2014, 4, 30, 10, 31, 15)}, {v: 2443.0} ] },
            {c: [ {v: new Date(2014, 4, 30, 10, 31, 30)}, {v: 2444.0} ] }
        ]
    };

    // create DataTable
    var data = new google.visualization.DataTable(jsonData);

    // create chart
    var chart = new google.visualization.LineChart(document.getElementById('chart-div'));

    chart.draw(data);

} // end drawChart()