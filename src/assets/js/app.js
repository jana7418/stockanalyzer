$(document).ready(function () {
    //Build the data table
    buildTable()

    //Set a event listner for index option change
    var index_option = $("#index_option").bind('change', function () {
        var index = index_option.val();
        fetchQuotes(index);    
    });

    index_option.trigger('change');  

    //Set a event listner for refresh checkbox change
    $("#refresh").click(function () {
        if ($(this).prop("checked") == true) {
            window.refreshCheckbox = setInterval(fetchQuotes, 30000);
        } else if ($(this).prop("checked") == false) {
            clearInterval(window.refreshCheckbox);
        }
    });

});

function fetchQuotes(index) {
    var api = "/api/get";
    $.ajax({
        url: api + '/index/' + index, success: function (obj) {
            obj.symbols.forEach(symbol => {
                var quote_url = api + '/stock/' + symbol;
                $.ajax({
                    url: quote_url,
                    success: function (quote) {
                        updateRow(symbol, quote)
                    }
                })
            });
        }
    });
}

function updateRow(symbol, quote) {
    var tableRow = $("#" + quote.symbol + "_row");
    var table = $('#table').DataTable();
    var rowObj = table.row(tableRow);
    var initialData = rowObj.data();
    var data = [
        initialData[0],
        quote.quote.priceInfo.lastPrice ? quote.quote.priceInfo.lastPrice : 0,
        quote.data.quantity.buy ? quote.data.quantity.buy : 0,
        quote.data.quantity.sell ? quote.data.quantity.sell : 0,
        ( quote.data.percent ? quote.data.percent : '0.00' ) + ' %',
    ];
    
    $("#" + quote.symbol + "_percent").addClass(quote.data.percent_cell_colour);
    rowObj.data(data).draw();
}

function buildTable() {
    $('#table').DataTable({
        "order": [[3, "desc"]],
        "paging": false
    });
}