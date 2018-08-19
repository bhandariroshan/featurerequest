$(document).ready(function () {
    function AppViewModel() {
        this.title = ko.observable("");
        this.description = ko.observable("");
        this.client = ko.observable("");
        this.priority = ko.observable("");
        this.targetDate = ko.observable("");
        this.productArea = ko.observable("");

        this.validateAndSubmit = function () {
            $.ajax("/feature/create/", {
                data: ko.toJSON({
                    'title': this.title(),
                    'description': this.description(),
                    'client': this.client(),
                    'priority': this.priority(),
                    'targetDate': this.targetDate(),
                    'productArea': this.productArea()
                }),
                type: "post", contentType: "application/json",
                success: function (result) {
                    alert(result['status']);
                }
            });

        };
    }

    // Activates knockout.js
    ko.applyBindings(new AppViewModel());
});