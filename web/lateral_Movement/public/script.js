var MorrisBarReturnObject;
var MorrisDonutReturnObject;

$(function() {

  Morris.Area({
    element: 'morris-area-chart',
    data: [{
      period: '2010 Q1',
      iphone: 2666,
      ipad: null,
      itouch: 2647
    }, {
      period: '2010 Q2',
      iphone: 2778,
      ipad: 2294,
      itouch: 2441
    }, {
      period: '2010 Q3',
      iphone: 4912,
      ipad: 1969,
      itouch: 2501
    }, {
      period: '2010 Q4',
      iphone: 3767,
      ipad: 3597,
      itouch: 5689
    }, {
      period: '2011 Q1',
      iphone: 6810,
      ipad: 1914,
      itouch: 2293
    }, {
      period: '2011 Q2',
      iphone: 5670,
      ipad: 4293,
      itouch: 1881
    }, {
      period: '2011 Q3',
      iphone: 4820,
      ipad: 3795,
      itouch: 1588
    }, {
      period: '2011 Q4',
      iphone: 15073,
      ipad: 5967,
      itouch: 5175
    }, {
      period: '2012 Q1',
      iphone: 10687,
      ipad: 4460,
      itouch: 2028
    }, {
      period: '2012 Q2',
      iphone: 8432,
      ipad: 5713,
      itouch: 1791
    }],
    xkey: 'period',
    ykeys: ['iphone', 'ipad', 'itouch'],
    labels: ['iPhone', 'iPad', 'iPod Touch'],
    pointSize: 2,
    hideHover: 'auto',
    resize: true
  });

  MorrisDonutReturnObject = Morris.Donut({
    element: 'morris-donut-chart',
    data: [{
      label: "Download Sales",
      value: 12
    }, {
      label: "In-Store Sales",
      value: 30
    }, {
      label: "Mail-Order Sales",
      value: 20
    }],
    resize: true
  });

  MorrisBarReturnObject = Morris.Bar({
    element: 'morris-bar-chart',
    data: [{
      y: 'ADEP',
      a: 16361.8,
    }, {
      y: 'EAD',
      a: 8205.05,
    }, {
      y: 'EID',
      a: 137.5,
    }, {
      y: 'EMD',
      a: 1296.05,
    }, {
      y: 'ESMD',
      a: 514,
    }, {
      y: 'EWD',
      a: 323.5,
    }, {
      y: 'ITMD',
      a: 454.5,
    }],
    xkey: 'y',
    ykeys: ['a'],
    labels: ['Actual Work'],
    hideHover: 'auto',
    resize: true
  });
  
  $('#morris-donut-chart cvg path').each(function(index) {
    addEventListener('mouseout', showDefaultDonutData());
  });

  $("#morris-bar-chart svg rect").on('click', function() {
    setFilterForBottomMorrisTable($(this));
  });

  $(window).resize(function() {
    $("#morris-bar-chart svg rect").on('click', function() {
      setFilterForBottomMorrisTable($(this));
    });
  });
  
});

var tableDataJson = {
  "headers": ["Directorate or Division", "Actual Work", "FTEs", "Resource Count"],
  "data": [{
    "Directorate or Division": "ADEP",
    "Actual Work": 16361.8,
    "FTEs": 32,
    "Resource Count": 64
  }, {
    "Directorate or Division": "EAD",
    "Actual Work": 8205.05,
    "FTEs": 16,
    "Resource Count": 25
  }, {
    "Directorate or Division": "EID",
    "Actual Work": 137.5,
    "FTEs": 0.27,
    "Resource Count": 1
  }, {
    "Directorate or Division": "EMD",
    "Actual Work": 1296.05,
    "FTEs": 2.53,
    "Resource Count": 8
  }, {
    "Directorate or Division": "ESMD",
    "Actual Work": 514,
    "FTEs": 1,
    "Resource Count": 4
  }, {
    "Directorate or Division": "EWD",
    "Actual Work": 323.5,
    "FTEs": 0.63,
    "Resource Count": 4
  }, {
    "Directorate or Division": "ITMD",
    "Actual Work": 454.5,
    "FTEs": 0.89,
    "Resource Count": 2
  }]
};

var allMorrisTableData = {
  "headers": ["Enterprise Projects", "Directorate or Division", "Actual Work", "FTEs", "Resource Count"],
  "data": [{
    "Enterprise Projects": "2020 Census Program Management",
    "Directorate or Division": "ITMD",
    "Actual Work": 418.50,
    "FTEs": 0.82,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "2020 Nonresponse Followup",
    "Directorate or Division": "ESMD",
    "Actual Work": 477.00,
    "FTEs": 0.93,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "2020 Response Processing",
    "Directorate or Division": "ADEP",
    "Actual Work": 277.50,
    "FTEs": 0.54,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "AHS 2015 Revised v1",
    "Directorate or Division": "ITMD",
    "Actual Work": 36.00,
    "FTEs": 0.07,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "CE Diary Survey 2016",
    "Directorate or Division": "ADEP",
    "Actual Work": 3.00,
    "FTEs": 0.01,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "CE Quarterly Survey 2016",
    "Directorate or Division": "ADEP",
    "Actual Work": 4.00,
    "FTEs": 0.01,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "CEDCaP-Electronic Correspondence Portal",
    "Directorate or Division": "EAD",
    "Actual Work": 1321.05,
    "FTEs": 2.58,
    "Resource Count": 9
  }, {
    "Enterprise Projects": "CEDCaP-Electronic Correspondence Portal",
    "Directorate or Division": "EMD",
    "Actual Work": 1294.05,
    "FTEs": 2.53,
    "Resource Count": 7
  }, {
    "Enterprise Projects": "CEDCaP-Questionnaire Design and Metadata-COMET",
    "Directorate or Division": "ADEP",
    "Actual Work": 3916.50,
    "FTEs": 7.65,
    "Resource Count": 11
  }, {
    "Enterprise Projects": "CEDCaP-Questionnaire Design and Metadata-COMET",
    "Directorate or Division": "EAD",
    "Actual Work": 3670.50,
    "FTEs": 7.17,
    "Resource Count": 8
  }, {
    "Enterprise Projects": "CEDCaP-Scanning Data Capture from Paper-ICADE",
    "Directorate or Division": "ADEP",
    "Actual Work": 7061.30,
    "FTEs": 13.79,
    "Resource Count": 27
  }, {
    "Enterprise Projects": "CEDCaP-Service Oriented Architecture-API",
    "Directorate or Division": "EAD",
    "Actual Work": 168.00,
    "FTEs": 0.33,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "CEDCaP-Survey and Listing Interview Operational Control-MOJO",
    "Directorate or Division": "ADEP",
    "Actual Work": 3768.25,
    "FTEs": 7.36,
    "Resource Count": 13
  }, {
    "Enterprise Projects": "CEDCaP-Survey and Listing Interview Operational Control-MOJO",
    "Directorate or Division": "EAD",
    "Actual Work": 3045.50,
    "FTEs": 5.95,
    "Resource Count": 7
  }, {
    "Enterprise Projects": "CEDCaP-Survey Response Processing-CARDS",
    "Directorate or Division": "ADEP",
    "Actual Work": 381.00,
    "FTEs": 0.74,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "CLMSO FY16 Education and Training",
    "Directorate or Division": "EWD",
    "Actual Work": 32.00,
    "FTEs": 0.06,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "FY2015 CPS 2014-2016 DSMD",
    "Directorate or Division": "ESMD",
    "Actual Work": 9.00,
    "FTEs": 0.02,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "HSDC2016",
    "Directorate or Division": "ADEP",
    "Actual Work": 13.50,
    "FTEs": 0.03,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "National Crime Victimization Survey SY 2015",
    "Directorate or Division": "ADEP",
    "Actual Work": 228.00,
    "FTEs": 0.45,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "National Crime Victimization Survey SY 2016",
    "Directorate or Division": "ADEP",
    "Actual Work": 420.25,
    "FTEs": 0.82,
    "Resource Count": 2
  }, {
    "Enterprise Projects": "National Crime Victimization Survey SY 2016",
    "Directorate or Division": "EID",
    "Actual Work": 137.50,
    "FTEs": 0.27,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "NHIS 2016",
    "Directorate or Division": "ESMD",
    "Actual Work": 18.00,
    "FTEs": 0.04,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "NHIS Administrative Schedule",
    "Directorate or Division": "ESMD",
    "Actual Work": 10.00,
    "FTEs": 0.02,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "NSCH 2016 Production",
    "Directorate or Division": "ADEP",
    "Actual Work": 241.00,
    "FTEs": 0.47,
    "Resource Count": 3
  }, {
    "Enterprise Projects": "NTPS 2015-2016",
    "Directorate or Division": "ADEP",
    "Actual Work": 47.50,
    "FTEs": 0.09,
    "Resource Count": 2
  }, {
    "Enterprise Projects": "NTPS 2015-2016",
    "Directorate or Division": "EMD",
    "Actual Work": 2.00,
    "FTEs": 0,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "z6385B10 CATI Response Data",
    "Directorate or Division": "EWD",
    "Actual Work": 153.00,
    "FTEs": 0.3,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "z6385B20 CAPI Response Data",
    "Directorate or Division": "EWD",
    "Actual Work": 114.50,
    "FTEs": 0.22,
    "Resource Count": 1
  }, {
    "Enterprise Projects": "z6385B30 PR Data Collection Data",
    "Directorate or Division": "EWD",
    "Actual Work": 24.00,
    "FTEs": 0.05,
    "Resource Count": 1
  }]
};

// This updates the data table beside the Morris.Bar 
function buildTable(localTableDataJson, tagId) {
  console.log('building table for ' + tagId);
  var content = "";
  var header = "<thead><tr>";
  console.log(localTableDataJson.headers)
  for (var index in localTableDataJson.headers) {
    console.log('added header');
    header += "<th>" + localTableDataJson.headers[index] + "</th>";
  }
  header += "</tr></thead>";
  content += header + "<tbody>";

  for (var index in localTableDataJson.data) {

    content += "<tr>";
    jQuery.each(localTableDataJson.data[index], function(index2, dataColumn) {
      content += "<td>" + dataColumn + "</td>";
    });
    content += "</tr>";

  }

  content += "</tbody>"

  $('#' + tagId).empty();
  $('#' + tagId).append(content);
}

buildTable(tableDataJson, 'first-morris-table');
buildTable(allMorrisTableData, 'second-morris-table');

var previousTagSelected;

function filterBottomMorrisTable(filterString, filterColumn) {
  console.log('filtering bottom Morris table for ' + filterString + ' in ' + filterColumn);
  console.log('previous tag: ' + previousTagSelected);
  if (filterString != previousTagSelected) {
    $('#second-morris-table > tbody > tr').each(function(index) {
      console.log('showing row');
      $(this).show();
    });
  }

  $('#second-morris-table > tbody > tr').each(
    function(index) {
      //console.log('table index ' + index);
      
      $(this).find('td').each(
        function(index2) {
          //console.log('column index ' + index2);
          var columnValue = $(this).text();
          //console.log('columnValue: ' + columnValue);
          var columnName = allMorrisTableData.headers[index2];
          //console.log('column name : ' + columnName);

          hideMorrisTable2Row($(this), columnName, columnValue, filterColumn, filterString);

        });

    }
  );
}

function hideMorrisTable2Row(selection, columnName, columnValue, filterColumn, filterString) {
  console.log('checking for ' + columnName + ' matching ' + filterColumn);
  if (columnName != filterColumn) {
    console.log(columnName + ' does not match' + filterColumn);
    return;
  }
  console.log(columnName + ' matches' + filterColumn);
  if ((columnValue != filterString) || (columnValue == '')) {
    console.log('toggle hiding table row for ' + columnValue);
    if ($(selection).parent().css('display') == 'none') {
      $(selection).parent().show();
      previousTagSelected = filterString;
    } else {
      $(selection).parent().hide();
    }
  } else {
    $(selection).parent().show();
    previousTagSelected = filterString;
  }
}


function  buildActionRequest(tenant, tag, typ, action, options) {
            var path;
            var request;
            path = "/api/1/";
            if (tenant && tag)
                path += tenant+tag + "/";
            path += typ + "?action\x3d" + action;
            request = {
                protocol: this.context.protocol,
                hostname: this.context.hostname,
                port: this.context.port,
                path: path,
                method: "POST",
                headers: {
                    "Accept": "application/json",
                    "Content-type": "application/json",
                }
            };
            if (this.context.authToken)
                request.headers.Authorization = this.context.authToken;
            if (this.context.tunnelTo)
                request.headers["X-Tunnel-To"] = this.context.tunnelTo;
            if (options) {
                if (options.headers)
                    Object.keys(options.headers).forEach(function(k) {
                        if (options.headers[k])
                            request.headers[k] = options.headers[k];
                        else
                            delete request.headers[k]
                    });
                if (options.method)
                    request.method = options.method;
                if (options.path)
                    request.path = options.path;
                if (options.data)
                    request.data = options.data
            }
            return request
 }


function updateMorrisBar(columnNumber) {
  console.log("updating morris bar");
  var newJSON = {
    element: 'morris-bar-chart',
    data: [{
      y: 'ADEP',
      a: 16361.8,
    }, {
      y: 'EAD',
      a: 8205.05,
    }, {
      y: 'EID',
      a: 137.5,
    }, {
      y: 'EMD',
      a: 1296.05,
    }, {
      y: 'ESMD',
      a: 514,
    }, {
      y: 'EWD',
      a: 323.5,
    }, {
      y: 'ITMD',
      a: 454.5,
    }],
    xkey: 'y',
    ykeys: ['a'],
    labels: ['Actual Work'],
    hideHover: 'auto',
    resize: true
  };
  switch (columnNumber) {
    case 1:
      for (var index in newJSON.data) {
        newJSON.data[index].a = tableDataJson.data[index]["Actual Work"];
      }
      newJSON.labels = ['Actual Work'];
      break;
    case 2:
      for (var index in newJSON.data) {
        newJSON.data[index].a = tableDataJson.data[index]["FTEs"];
      }
      newJSON.labels = ['FTEs'];
      break;
    case 3:
      for (var index in newJSON.data) {
        newJSON.data[index].a = tableDataJson.data[index]["Resource Count"];
      }
      newJSON.labels = ['Resource Count'];
      break;
  }

  $('#morris-bar-chart').empty();
  Morris.Bar(newJSON);
  //MorrisBarReturnObject.setData(newJSON);
  MorrisBarReturnObject.setData(newJSON.data, true);

  $("#morris-bar-chart svg rect").on('click', function() {
    //alert( "Handler for .on() called." );
    setFilterForBottomMorrisTable($(this));
  });
}

function setFilterForBottomMorrisTable(selectedTag) {
  var tagIndex = $('#morris-bar-chart svg rect').index(selectedTag);
  console.log('tag index: ' + tagIndex);
  var name = tableDataJson.data[tagIndex]['Directorate or Division'];
  console.log('Directorate or Division name: ' + name);
  filterBottomMorrisTable(name, 'Directorate or Division');
  showTotalFTEs();
}

// shows the total FTEs in the morris donut
function showTotalFTEs() {
  console.log('updating donut data');
  var totalFTEs = 0;
  var totalAmountWorked = 0;
  var totalResourceCount = 0;
  $('#second-morris-table > tbody > tr').each(
    function(index) {
      //console.log('table index ' + index);
      $(this).find('td').each(
        function(index2) {
          if ($(this).parent().css('display') != 'none') {
            if (allMorrisTableData.headers[index2] == 'FTEs') {
              totalFTEs += parseFloat($(this).text());
            }
            if (allMorrisTableData.headers[index2] == 'Actual Work') {
              totalAmountWorked += parseFloat($(this).text());
            }
            if (allMorrisTableData.headers[index2] == 'Resource Count') {
              totalResourceCount += parseFloat($(this).text());
            }
          }
        });
    });
  
  var donutJSON = {
    element: 'morris-donut-chart',
    data: [{
      label: "Total FTEs",
      value: totalFTEs.toFixed(2)
    }/*, {
      label: "Total Amount Worked",
      value: totalAmountWorked.toFixed(2)
    }, {
      label: "Total Resource Count",
      value: totalResourceCount.toFixed(2)
    }*/],
    resize: true
  };
  
  $('#morris-donut-chart').empty();
  Morris.Donut(donutJSON);
  //MorrisBarReturnObject.setData(newJSON);
  MorrisDonutReturnObject.setData(donutJSON.data, true);
}


function showDefaultDonutData() {
  console.log('leaving svg donut part');
}
