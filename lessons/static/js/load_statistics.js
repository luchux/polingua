google.load("visualization", "1", {packages:["corechart","geochart"]});
google.setOnLoadCallback(drawChart2());
//This script loads the statistics and generate API charts. 

function drawChart2() {

	$.getJSON("/polingua/stats",function(datos){
      //data = createData(datos)
      	var data = new google.visualization.DataTable();
        data.addColumn('string', 'Word');
        data.addColumn('number', 'Learned');
        data.addRows(datos);
		var options = {
			title: 'Words most learned',
			vAxis: {title: 'Words',  titleTextStyle: {color: 'green'}}
		};

        var chart2 = new google.visualization.ColumnChart(document.getElementById('div_stats1'));
        chart2.draw(data, options);

        var chart3 = new google.visualization.PieChart(document.getElementById('div_stats2'));
        chart3.draw(data, options);

        var chart4 = new google.visualization.LineChart(document.getElementById('div_stats3'));
        chart4.draw(data, options);
  	});
};

