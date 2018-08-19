$(document).ready(function () {
    var features;
    $.post("/feature/getall/", function (data) {
        features = data['data'];
        ko.applyBindings({
        features: features
    });
    });
});