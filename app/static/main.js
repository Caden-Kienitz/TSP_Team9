let IPA_result = "";
let data_file = 'static/en_us.json';

function update_result() {
  let c_w = (get_IPA_tBox() + " ").split(" ");

  set_IPA_tBox("loading....");

  get_IPA_DB(IPA_db => {
      let str = "";
      for (let i = 0; i < c_w.length; i++) {
          let word = c_w[i].toLowerCase().replace(/[^\w\s]/gi, '');
          if (word != "") {
              if (IPA_db[word]) {
                  str += IPA_db[word] + " ";
              } else {
                  str += word + " ";
              }
          }
      }
      set_IPA_tBox(str);
  });
}


function get_IPA_DB(callback) {
  console.log('get_IPA_DB called'); // Add this line
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var myObj = JSON.parse(this.responseText);
      var IPA_db = myObj['en_US'][0]; // access the IPA database for en_US
      callback(IPA_db); // call the callback function with the IPA_db value
    }
  };

  xmlhttp.open("GET", "static/en_us.json", true);
  xmlhttp.send();
}



function get_IPA_tBox () {
  return document.getElementById("cWords_tBox").value
}

function set_IPA_tBox (v = IPA_result) {
  console.log('set_IPA_tBox called with value:', v); // Add this line
  document.getElementById("IPA_tBox").value = v;
}


update_result ();