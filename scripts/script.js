const articleDataFromFile = [
    {
        id: 1,
        imageSrc: 'statics/dish1.png',
        imageAlt: 'Spaghetti',
        category: 'Food',
        title: 'Spaghetti',
        excerpt: 'Historia spaghetti: Spaghetti jest tradycyjną włoską potrawą, która pochodzi z regionu Neapolu. Pierwsze wzmianki o spaghetti można znaleźć w dokumentach datowanych na XIII wiek. Współcześnie spaghetti jest popularne na całym świecie i jest podawane w różnych wariantach z różnymi sosami i dodatkami.',
        allergens: "allergens",
        how2: "how2",
        others: "others"
    },  
    {
        id: 2,
        imageSrc: 'statics/dish2.png',
        imageAlt: 'Salad',
        category: 'Food',
        title: 'Salad',
        excerpt: 'Historia sałatki: Sałatka jest lekkim daniem składającym się z różnych świeżych składników takich jak warzywa, owoce, mięso lub ryby. Pierwsze sałatki pojawiły się już w starożytności, gdzie były spożywane jako środek na ochłodzenie organizmu. Obecnie sałatki są szeroko rozpowszechnione i istnieje wiele różnych rodzajów sałatek z różnymi składnikami i sosami.'
    },
    {   
        id: 3,
        imageSrc: 'statics/dish3.png',
        imageAlt: 'Pizza',
        category: 'Food',
        title: 'Pizza',
        excerpt: 'Historia pizzy: Pizza jest klasycznym daniem włoskim, które ma długą historię sięgającą starożytności. Pierwsze wzmianki o podobnych daniach do pizzy pochodzą z czasów starożytnego Egiptu i Grecji. Jednak współczesna pizza, z charakterystycznym ciastem z pomidorowym sosem i różnymi dodatkami, wywodzi się z Neapolu w XIX wieku. Dziś pizza jest jednym z najpopularniejszych dań na świecie.'
    },
    {
        id: 4,
        imageSrc: 'statics/dish4.png',
        imageAlt: 'Burger',
        category: 'Food',
        title: 'Burger',
        excerpt: 'Historia burgera: Burger, znany również jako hamburger, jest popularnym daniem fast foodowym. Pierwsze hamburgery zaczęły się pojawiać w XIX wieku w Stanach Zjednoczonych. Powszechnie uważa się, że pierwszy hamburger został stworzony w 1900 roku przez Louisa Laskera, który otworzył swoją restaurację w New Haven, Connecticut. Od tego czasu hamburgery zdobyły ogromną popularność i stały się symbolem kultury fast foodowej.'
    },
    {
        id: 5,
        imageSrc: 'statics/dish5.png',
        imageAlt: 'Sushi',
        category: 'Food',
        title: 'Sushi',
        excerpt: 'Historia sushi: Sushi jest tradycyjnym japońskim daniem, które ma ponad 1000 lat historii. Pierwsze formy sushi pojawiły się w VIII wieku w Japonii i były używane jako sposób na przechowywanie ryb w fermentowanym ryżu. Wraz z upływem czasu sushi ewoluowało i różne style sushi powstały w różnych regionach Japonii. Dziś sushi jest popularne na całym świecie i jest znane ze swojej świeżości, precyzji i różnorodności.'
    },
    {
        id: 6,
        imageSrc: 'statics/dish6.png',
        imageAlt: 'Taco',
        category: 'Food',
        title: 'Taco',
        excerpt: 'Historia taco: Taco jest tradycyjnym meksykańskim daniem, które ma długą historię sięgającą czasów prekolumbijskich. Pierwsze tacos były przygotowywane przez Azteków i Mayów, którzy używali tortilli do owinięcia różnych składników, takich jak mięso, warzywa i owoce morza. Tacos zyskały popularność w Meksyku i zostały przyjęte przez inne kultury na całym świecie. Dziś taco jest jednym z najbardziej rozpoznawalnych dań meksykańskich.'
    },
    {
        id: 7,
        imageSrc: 'statics/dish7.png',
        imageAlt: 'Pierogi',
        category: 'Food',
        title: 'Pierogi',
        excerpt: 'Historia pierogów: Pierogi są tradycyjnym daniem kuchni słowiańskiej, szczególnie popularnym w Polsce, Rosji, Ukrainie i innych krajach regionu. Pierwsze wzmianki o pierogach pochodzą z XIII wieku, ale przepis na pierogi był przekazywany z pokolenia na pokolenie przez wieki. Pierogi są małymi pierożkami, które są wypełnione różnymi składnikami, takimi jak mięso, kapusta, ser, owoce i inne. Są gotowane lub smażone i często podawane z sosem.'
    },
    {
        id: 8,
        imageSrc: 'statics/dish8.png',
        imageAlt: 'Curry',
        category: 'Food',
        title: 'Curry',
        excerpt: 'Historia curry: Curry to popularne danie z kuchni indyjskiej, które ma długą historię sięgającą tysiące lat. Pierwsze wzmianki o curry można znaleźć w starożytnych tekstach indyjskich datowanych na IV wiek p.n.e. Curry składa się z różnych przypraw, takich jak kurkuma, kolendra, cynamon, kardamon i inne, które są używane do przygotowania aromatycznego sosu. Curry jest podawane z różnymi składnikami, takimi jak mięso, ryby, warzywa i ryż.'
    }, 
    {
        id: 9,
        imageSrc: 'statics/dish9.png',
        imageAlt: 'Steak',
        category: 'Food',
        title: 'Steak',
        excerpt: 'Historia steka: Steak jest popularnym daniem mięsnym, szczególnie cenionym przez miłośników wołowiny. Historia steka sięga starożytnych czasów, kiedy to ludzie zaczęli spożywać mięso z zwierząt łownych. Jednak jako potrawa specjalna i rytualna, przygotowanie steka zaczęło się rozwijać wraz z rozwojem technik kulinarnych i sztuki grillowania. Dziś stek jest często podawany z różnymi dodatkami, takimi jak sosy, warzywa czy ziemniaki.'
    },  
    {
        id: 10,
        imageSrc: 'statics/dish10.png',
        imageAlt: 'Kebab',
        category: 'Food',
        title: 'Kebab',
        excerpt: 'Historia kebaba: Kebab jest tradycyjnym daniem kuchni Bliskiego Wschodu, które ma długą historię sięgającą starożytności. Pierwsze wzmianki o kebabie można znaleźć w starożytnych tekstach perskich datowanych na I tysiąclecie p.n.e. Kebab składa się z kawałków mięsa, takich jak wołowina, baranina, kurczak lub mięso mielone, które są grillowane na rożnie lub smażone. Kebab jest często podawany wraz z warzywami, sałatkami i sosem.'
    }

];

//import {articleDataFromFile} from './data.js';

const articleContainer = document.getElementsByClassName('article-container')[0];

function createArticleElement(data) {
    const article = document.createElement('article');
    const figure = document.createElement('figure');
    const img = document.createElement('img');
    const div = document.createElement('div');
    const a = document.createElement('a');
    const h3 = document.createElement('h3');
    const p = document.createElement('p');

    article.className = 'article-card';
    article.id = data.id;
    figure.className = 'article-image';
    div.className = 'article-content';
    a.className = 'card-category';
    h3.className = 'card-title';
    p.className = 'card-excerpt';

    img.src = data.imageSrc;
    img.alt = data.imageAlt;
    a.href = '#';
    a.textContent = data.category;
    h3.textContent = data.title;
    p.textContent = data.excerpt;

    figure.appendChild(img);
    div.appendChild(a);
    div.appendChild(h3);
    div.appendChild(p);
    article.appendChild(figure);
    article.appendChild(div);

    return article;
}

function renderArticles() {
    articleDataFromFile.forEach((data, index) => {
        data.id = index+1;
        const article = createArticleElement(data);
        articleContainer.appendChild(article);
    });
}

function filterContentByString() {
    const inputValue = document.querySelector('input[name="q"]').value.toLowerCase();
    const articles = articleContainer.getElementsByClassName('article-card');

    Array.from(articles).forEach(article => {
        const title = article.querySelector('.card-title').textContent.toLowerCase();
        const excerpt = article.querySelector('.card-excerpt').textContent.toLowerCase();
        const category = article.querySelector('.card-category').textContent.toLowerCase();

        if (title.includes(inputValue) || excerpt.includes(inputValue)  || category.includes(inputValue)) {
            article.style.display = 'block';
        } else {
            article.style.display = 'none';
        }
    });
}

renderArticles();


function WhichDetailCategory(category) {
    document.getElementById('ShowingDetails').setAttribute('name', category);
}

const basicActiveDetail = {
    Allegrens: 'Opis Allegrens',
    How2: 'Opis How2',
    Others: 'Opis Others'
  };
  
function showArticleDetails(event) {
    var activeDetail = document.getElementById('ShowingDetails');

    if (!event.currentTarget){
        activeDetail.innerHTML = basicActiveDetail[event];
        activeDetail.setAttribute('name', event);
    }
    else{
        const articleCard = event.currentTarget;
        const articleData = articleDataFromFile.find(data => data.id == articleCard.id);

        if (activeDetail.getAttribute('name') == "Allegrens")
            activeDetail.innerHTML = articleData.allergens;

        if (activeDetail.getAttribute('name') == "How2")
            activeDetail.innerHTML = articleData.how2;

        if (activeDetail.getAttribute('name') == "Others")
            activeDetail.innerHTML = articleData.others;
    }
}





const articleCards = document.getElementsByClassName('article-card');
Array.from(articleCards).forEach(card => {
    card.addEventListener('click', showArticleDetails);
});