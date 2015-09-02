/**
 * Created by Maxwell J. Resnick on 9/1/15.
 */
// Overkill for this assignment
var $jQ = jQuery.noConflict();

var form = {
    name: function (name) {
            this.isValid = /^([a-zA-Z]+)$/
                    .test(name);
            this.error = "Your name must be chars only.";
            if (!this.isValid) {
                error = this.error;
            }
            return this.isValid;
          },
    username: function (username) {
            this.isValid = /^[a-zA-Z]+[\w\.][a-zA-Z0-9]+$/
                    .test(username);
            this.error = "Your name must be number, chars, and _ only.";
            if (!this.isValid) {
                error = this.error;
            }
            return this.isValid;
          },
    email: function (email) {
            this.isValid = /^[a-zA-Z]+[\w\._+]+@([^\.]\w*\.)*[a-zA-Z]*[a-zA-Z]$/
                    .test(email);
            this.error = "You must have a valid email address.";
            if (!this.isValid) {
                error = this.error;
            }
            return this.isValid;
          },
    error: null,
};


function formHandler($e) {
    this.form = new form;
    $e.each(function () {
            if (!form[this.name](this.value)) {
                $jQ(this).after(function () {
                        return '<div class="error">' + form.error + '</div>';
                    });
            } else {
                $jQ(this).next('.error').remove();
            }
        });
};

(function () {
    /*
     * @description make my error class.
     */

    this.sheet = document.styleSheets[0];
    this.errorStyle = (".error {" +
                       "background-color: tomato;" +
                       "color: #fff;" +
                       "size: .75em;" +
                       "padding: 10px;" +
                       "margin: 10px;" +
                       "border-radius: 5px; }");
    this.sheet.insertRule(this.errorStyle, 0);
}());
$jQ(function () {
    /*
     * @description event bindings.
     */
    $jQ('#signup').on({
        'submit': function(e){
            e.preventDefault();
            var toCheck = $jQ(e.target).children('input').not("#submit");
            if(formHandler(toCheck)) {
                registerUser();
            };
        },
        'change': function(e){
            var toCheck = $jQ(e.target);
            formHandler(toCheck);
        }
    });
}());