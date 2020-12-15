const CUPCAKES_ENDPOINT = "/api/cupcakes";
const $cupcakeList = $("#cupcake-list");
const $cupcakeForm = $("#cupcake-form");

/**
 * Calls fetchCupcakeList to get the cupcakes
 * calls generatemarkup and appends it to the DOM
 */
async function showCupcakesOnPage() {
  let cupcakeList = await fetchCupcakeList()
  for (let cupcake of cupcakeList) {
    let html = generateMarkup(cupcake);
    $cupcakeList.append(html);
  }
}
/* GET request to display all the cupcakes
 */
async function fetchCupcakeList() {
  const response = await axios.get(CUPCAKES_ENDPOINT);
  return response.data.cupcakes;
}

/* Genereate markup for a cupcake
 */
function generateMarkup(cupcake) {
  let html = `<li class="list-group">
                <div class="list-group-item">
                  <h5 class=mb-1">Flavor: ${cupcake.flavor}</h5>
                  <img class="img-thumbnail list-group-item lw-25" src="${cupcake.image}">
                  <p class="mb-1">Size: ${cupcake.size}, Rating: ${cupcake.rating}</p>
                </div>
              </li>`;
  return html;
}

/* Grabs form data then sends AJAX request to
 * POST /api/cupcakes
 * which adds a cupcake
 */
async function handleFormData(evt) {
  evt.preventDefault();
  // Get form data
  let flavor = $("#flavor").val();
  let size = $("#size").val();
  let rating = $("#rating").val();
  let image = $("#image").val();
  let cupcakeFormData = { flavor, size, rating, image };

  // Return the request reponse
  let cupcake = await axios.post(CUPCAKES_ENDPOINT, cupcakeFormData);
  // Add cupcake to page
  generateMarkupAndAppend(cupcake.data.cupcake);

  document.querySelector("#cupcake-form").reset();
}

fetchCupcakeList();

$cupcakeForm.on("submit", handleFormData)
