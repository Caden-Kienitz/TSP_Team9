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

/*function preprocess_eng (x,callback){
  x = x.replace(/A/g, "a");
  x = x.replace(/B/g, "b");
  x = x.replace(/C/g, "c");
  x = x.replace(/D/g, "d");
  x = x.replace(/E/g, "e");
  x = x.replace(/F/g, "f");
  x = x.replace(/G/g, "g");
  x = x.replace(/H/g, "h");
  x = x.replace(/I/g, "i");
  x = x.replace(/J/g, "j");
  x = x.replace(/K/g, "k");
  x = x.replace(/L/g, "l");
  x = x.replace(/M/g, "m");
  x = x.replace(/N/g, "n");
  x = x.replace(/O/g, "o");
  x = x.replace(/P/g, "p");
  x = x.replace(/Q/g, "q");
  x = x.replace(/R/g, "r");
  x = x.replace(/S/g, "s");
  x = x.replace(/T/g, "t");
  x = x.replace(/U/g, "u");
  x = x.replace(/V/g, "v");
  x = x.replace(/W/g, "w");
  x = x.replace(/X/g, "x");
  x = x.replace(/Y/g, "y");
  x = x.replace(/Z/g, "z");
  x = x.replace(/\./g, "");
  x = x.replace(/\,/g, "");
  x = x.replace(/\n/g, "");
  callback(x);
}*/

update_result ();