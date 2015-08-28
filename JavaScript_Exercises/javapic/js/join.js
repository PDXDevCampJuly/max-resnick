/**
 * Created by Maxwell J. Resnick on 8/27/15.
 * join
 * ----
 * validate name
 * validate username
 * validate email
 * allow to submission, and redirect to the next page
 */


    function validate(e) {
    /*
     * @description validates form
     */
    this.fieldsToValidate = e;
    this.validation = null;
    if (this.fieldsToValidate.getAttribute('name') === 'name') {
        // REGEX
        var name = /^[a-zA-Z]+[a-zA-Z ]+[a-zA-Z]$/
            .test(this.fieldsToValidate.value);
        // Going to explicitly test for true and false. What if it's all janky?
        if (!name) {
            this.validation = false;
        } else if (name) {
            this.validation = true;
        }
        this.validation = true;
    } else if (this.fieldsToValidate.getAttribute('name') === 'email') {
        /*
         * ^[a-zA-Z] - email usernamesstart w/ alpha only
         * [\w\._+] any alphanumeric but also "." "_" "+" are valid specials for usernames.
         * must be a @
         * any number of domains, subdomains as long as we end with a char.
         */
        var email = /^[a-zA-Z]+[\w\._+]+@([^\.]\w*\.)*[a-zA-Z]*[a-zA-Z]$/
            .test(this.fieldsToValidate.value);
        if (!email) {
            this.validation = false;
        } else if (email) {
            this.validation = true;
        }

    } else if (this.fieldsToValidate.getAttribute('name') === 'username') {
        // REGEX
        var username = /^[a-zA-Z]+[\w\.][a-zA-Z0-9]$/
            .test(this.fieldsToValidate.value);
        if (!username) {
            this.validation = false;
        } else if (username){
            this.validation = true;
        }
    }
    console.log(this.validation);
}

// Event Binding
var form = document.getElementById('signup');
form.addEventListener('change', function(e){
    validate(e.target);
});