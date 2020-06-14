$(document).ready(function () {
    buildTable()
    fetchQuotes()
    $("#refresh").click(function () {
        if ($(this).prop("checked") == true) {
            window.refreshCheckbox = setInterval(fetchQuotes, 30000);
        } else if ($(this).prop("checked") == false) {
            clearInterval(window.refreshCheckbox);
        }
    });
});

function fetchQuotes() {
    var api = "/api/get";
    $.ajax({
        url: api, success: function (obj) {
            obj.symbols.forEach(symbol => {
                var quote_url = api + '/' + symbol;
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
    var data = [
        symbol,
        quote.data.quantity.buy ? quote.data.quantity.buy : 0,
        quote.data.quantity.sell ? quote.data.quantity.sell : 0,
        quote.data.percent ? quote.data.percent : '0.00' + ' %',
    ];
    var tableRow = $("#" + quote.symbol + "_row");
    $("#" + quote.symbol + "_percent").addClass(quote.data.percent_cell_colour);
    var table = $('#table').DataTable();
    table.row(tableRow).data(data).draw();
}

function buildTable() {
    $('#table').DataTable({
        "order": [[3, "desc"]]
    });
}