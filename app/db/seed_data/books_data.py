books_data = [
    {'book_title': 'The Alchemist',
  'page_count': 208,
  'publish_date': '1988-05-01',
  'price': 14.95,
  'description': 'A philosophical book that tells the story of Santiago, an Andalusian shepherd boy who yearns to travel in search of a worldly treasure.',
  'inventory_count': 12,
  'isbn': '9780062315007',
  'author_id': '779fa00a-09d6-444e-9ce8-540e65ac5e19'},

 {'book_title': 'Pride and Prejudice',
  'page_count': 432,
  'publish_date': '1813-01-28',
  'price': 9.99,
  'description': 'The novel follows the character development of Elizabeth Bennet, the dynamic protagonist, who learns about the repercussions of hasty judgments and comes to appreciate the difference between superficial goodness and actual goodness.',
  'inventory_count': 74,
  'isbn': '9781503290563',
  'author_id': '8283a8d6-e43b-4e48-8b4b-229e7a3f9a7f'},

 {'book_title': 'Adventures of Huckleberry Finn',
  'page_count': 366,
  'publish_date': '1884-12-10',
  'price': 8.99,
  'description': 'Direct sequel to The Adventures of Tom Sawyer. The book is noted for its colorful description of people and places along the Mississippi River.',
  'inventory_count': 81,
  'isbn': '9780486400778',
  'author_id': '78f2351f-8786-45f6-8e8e-78d3dc51e9fa'},

 {'book_title': 'Mrs. Dalloway',
  'page_count': 194,
  'publish_date': '1925-05-14',
  'price': 7.99,
  'description': "Details a day in the life of Clarissa Dalloway, a fictional high-society woman in post–First World War England. It is one of Woolf's best-known novels.",
  'inventory_count': 87,
  'isbn': '9780156628709',
  'author_id': 'a41e87a3-ed5a-432b-88e8-ac5d971f1c36'},

 {'book_title': 'Anna Karenina',
  'page_count': 864,
  'publish_date': '1877-04-01',
  'price': 12.99,
  'description': "Tolstoy's Anna Karenina tells of the doomed love affair between the sensuous and rebellious Anna and the dashing officer, Count Vronsky.",
  'inventory_count': 67,
  'isbn': '9781400079988',
  'author_id': '19730510-9a97-4ce9-a39d-506bb7ff1a8f'},

 {'book_title': 'Warrior of the Light',
  'page_count': 160,
  'publish_date': '2003-03-30',
  'price': 16.99,
  'description': 'A manual that teaches the reader, through stories and reflections, how to embrace the warrior of the light within themselves.',
  'inventory_count': 36,
  'isbn': '9780060527983',
  'author_id': '779fa00a-09d6-444e-9ce8-540e65ac5e19'},

 {'book_title': 'Emma',
  'page_count': 544,
  'publish_date': '1815-12-25',
  'price': 11.99,
  'description': 'A novel about youthful hubris and the perils of misconstrued romance, the story explores the concerns and difficulties of genteel women living in Georgian–Regency England.',
  'inventory_count': 41,
  'isbn': '9780141439587',
  'author_id': '8283a8d6-e43b-4e48-8b4b-229e7a3f9a7f'},

 {'book_title': 'Life on the Mississippi',
  'page_count': 624,
  'publish_date': '1883-01-01',
  'price': 13.95,
  'description': "A memoir of Twain's experiences as a steamboat pilot on the Mississippi River before the American Civil War, and a travel book, recounting his trip down the Mississippi River from St. Louis to New Orleans many years after the War.",
  'inventory_count': 6,
  'isbn': '9780486414263',
  'author_id': '78f2351f-8786-45f6-8e8e-78d3dc51e9fa'},

 {'book_title': 'Orlando',
  'page_count': 256,
  'publish_date': '1928-10-11',
  'price': 14.95,
  'description': "A semi-biographical novel based in part on the life of Woolf's lover Vita Sackville-West, it is generally considered one of Woolf's most accessible novels.",
  'inventory_count': 36,
  'isbn': '9780156701600',
  'author_id': 'a41e87a3-ed5a-432b-88e8-ac5d971f1c36'},
 {'book_title': 'The Death of Ivan Ilyich',
  'page_count': 86,
  'publish_date': '1886-02-01',
  'price': 10.0,
  'description': 'A novella by Leo Tolstoy, considered one of the masterpieces of his late fiction, written shortly after his religious conversion of the late 1870s.',
  'inventory_count': 29,
  'isbn': '9780486435091',
  'author_id': '19730510-9a97-4ce9-a39d-506bb7ff1a8f'},
    {
    "book_title": "The Brothers Karamazov",
    "page_count": 796,
    "publish_date": "1880-11-01",
    "price": 15.95,
    "description": "The final novel by Dostoevsky delves into the lives of the troubled Karamazov family, exploring deep philosophical questions of faith, doubt, and reason.",
    "inventory_count": 72,
    "isbn": "9780486437913",
    "author_id": "cc198234-0a02-4299-bd2f-fdba9edfbbf8"
  },
  {
    "book_title": "Notes from Underground",
    "page_count": 136,
    "publish_date": "1864-01-01",
    "price": 6.95,
    "description": "A short and powerful novel that introduces Dostoevsky's most important themes—psychological depth, existential despair, and the quest for meaning in a seemingly indifferent world.",
    "inventory_count": 85,
    "isbn": "9780486270531",
    "author_id": "cc198234-0a02-4299-bd2f-fdba9edfbbf8"
  },
  {
    "book_title": "For Whom the Bell Tolls",
    "page_count": 480,
    "publish_date": "1940-10-21",
    "price": 17.00,
    "description": "Set against the backdrop of the Spanish Civil War, Hemingway's novel explores themes of love, loss, and the harsh realities of war.",
    "inventory_count": 63,
    "isbn": "9780684803357",
    "author_id": "ae4b05b4-5e7b-44dc-9851-e8be1c36a79d"
  },
  {
    "book_title": "A Farewell to Arms",
    "page_count": 332,
    "publish_date": "1929-09-01",
    "price": 16.00,
    "description": "A novel of love and war, telling the story of an American ambulance driver on the Italian front and his passion for a beautiful English nurse.",
    "inventory_count": 57,
    "isbn": "9780142437339",
    "author_id": "ae4b05b4-5e7b-44dc-9851-e8be1c36a79d"
  },
  {
    "book_title": "The Hobbit",
    "page_count": 310,
    "publish_date": "1937-09-21",
    "price": 14.99,
    "description": "Bilbo Baggins, a hobbit enjoying his quiet life, is thrust into an epic quest by the wizard Gandalf and a group of dwarves to reclaim their mountain home from a dragon.",
    "inventory_count": 94,
    "isbn": "9780547928227",
    "author_id": "b79427dc-0222-4547-8392-07cedf7a3e74"
  },
  {
    "book_title": "Animal Farm",
    "page_count": 112,
    "publish_date": "1945-08-17",
    "price": 9.99,
    "description": "A farm is taken over by its overworked, mistreated animals. With flaming idealism and stirring slogans, they set out to create a paradise of progress, justice, and equality.",
    "inventory_count": 88,
    "isbn": "9780451526342",
    "author_id": "2c7320aa-327a-4d3f-bd77-67fd4e9415ce"
  },
  {
    "book_title": "As I Lay Dying",
    "page_count": 267,
    "publish_date": "1930-10-06",
    "price": 14.95,
    "description": "The novel tells the story of the death of Addie Bundren and her poor, rural family's quest and motivations—noble or selfish—to honor her wish to be buried in the town of Jefferson.",
    "inventory_count": 50,
    "isbn": "9780679732259",
    "author_id": "9e668a21-9cd9-4c4f-aa01-76993332fec5"
  },
  {
    "book_title": "The Sound and the Fury",
    "page_count": 326,
    "publish_date": "1929-10-07",
    "price": 15.00,
    "description": "This novel captures the lives of the Compson family, focusing on the decline of the once-aristocratic clan and the fading of their Southern traditions, seen through the eyes of three brothers.",
    "inventory_count": 77,
    "isbn": "9780679732242",
    "author_id": "9e668a21-9cd9-4c4f-aa01-76993332fec5"
  },
    {
    "book_title": "Murder on the Orient Express",
    "page_count": 256,
    "publish_date": "1934-01-01",
    "price": 14.99,
    "description": "A classic mystery novel featuring the Belgian detective Hercule Poirot, who investigates a murder aboard the famous train. Christie's ingenious plot twists will keep you guessing until the very end.",
    "inventory_count": 90,
    "isbn": "9780062693662",
    "author_id": "f320efd3-ba7d-41ab-bf02-503189318d63"
  },
  {
    "book_title": "Ulysses",
    "page_count": 730,
    "publish_date": "1922-02-02",
    "price": 23.00,
    "description": "Joyce's groundbreaking novel chronicles the peripatetic appointments and encounters of Leopold Bloom in Dublin in the course of an ordinary day, 16 June 1904.",
    "inventory_count": 70,
    "isbn": "9780141182803",
    "author_id": "e510348a-d8bd-4b1d-bcde-a4e8f30aef1d"
  },
  {
    "book_title": "The Trial",
    "page_count": 304,
    "publish_date": "1925-01-01",
    "price": 12.95,
    "description": "Kafka's nightmarish tale of a man arrested and prosecuted by a remote, inaccessible authority, with the nature of his crime revealed neither to him nor the reader.",
    "inventory_count": 80,
    "isbn": "9780805209990",
    "author_id": "ab25f66b-2b22-4f27-ac88-5526e2359d4f"
  },
  {
    "book_title": "Beloved",
    "page_count": 324,
    "publish_date": "1987-09-01",
    "price": 16.00,
    "description": "Morrison's novel examines the haunting legacy of slavery, as a mother makes a horrifying choice out of love that resonates across generations.",
    "inventory_count": 85,
    "isbn": "9781400033416",
    "author_id": "60c07ad1-f495-412c-9d6a-268497cc9864"
  },
  {
    "book_title": "One Hundred Years of Solitude",
    "page_count": 417,
    "publish_date": "1967-06-05",
    "price": 18.99,
    "description": "Márquez's epic tells the story of the Buendía family over seven generations, blending the magical and the real in a vividly painted Colombian landscape.",
    "inventory_count": 95,
    "isbn": "9780060883287",
    "author_id": "f3d83e18-6d8d-4e34-a27c-f9a02d26e5ec"
  },
    {
    "book_title": "Norwegian Wood",
    "page_count": 296,
    "publish_date": "1987-09-04",
    "price": 15.00,
    "description": "A poignant story of one college student's romantic coming-of-age, Norwegian Wood takes us to that distant place of a young man's first, hopeless, and heroic love.",
    "inventory_count": 85,
    "isbn": "9780375704024",
    "author_id": "8d820051-04b1-4d4f-999b-4c762a023286"
  },
  {
    "book_title": "1Q84",
    "page_count": 928,
    "publish_date": "2009-05-29",
    "price": 22.95,
    "description": "An ode to George Orwell's '1984' told in a world with two moons, 1Q84 is a fascinating, complex novel of love, terror, and longing.",
    "inventory_count": 75,
    "isbn": "9780307593313",
    "author_id": "8d820051-04b1-4d4f-999b-4c762a023286"
  },
  {
    "book_title": "Harry Potter and the Chamber of Secrets",
    "page_count": 341,
    "publish_date": "1998-07-02",
    "price": 12.99,
    "description": "The second installment in the Harry Potter series finds Harry and his friends facing new challenges, including the legend of the Chamber of Secrets.",
    "inventory_count": 93,
    "isbn": "9780439064873",
    "author_id": "d063d6d6-4fb8-4e3b-9d9a-b8e9a70b2d29"
  },
  {
    "book_title": "The Stand",
    "page_count": 1153,
    "publish_date": "1978-10-03",
    "price": 18.00,
    "description": "Stephen King's apocalyptic vision of a world blasted by plague and embroiled in an elemental struggle between good and evil.",
    "inventory_count": 80,
    "isbn": "9780307743688",
    "author_id": "0cab471e-fda3-41f7-a936-cdfcd8f35154"
  },
  {
    "book_title": "And Still I Rise",
    "page_count": 67,
    "publish_date": "1978-08-17",
    "price": 17.00,
    "description": "Maya Angelou's third volume of poetry is a powerful collection that spans many years of her life. Her heartfelt and poignant poems speak to the resilience of the human spirit.",
    "inventory_count": 62,
    "isbn": "9780394502526",
    "author_id": "e1bba2d8-9338-4ced-9f66-9611eee9dbe5"
  },
  {
    "book_title": "Cat's Cradle",
    "page_count": 304,
    "publish_date": "1963-04-11",
    "price": 15.95,
    "description": "Vonnegut's satirical commentary on modern man and his madness. An apocalyptic tale of this planet's ultimate fate, it features a midget as the protagonist.",
    "inventory_count": 88,
    "isbn": "9780385333481",
    "author_id": "a303ae3e-c2be-4a19-80b8-1b28bc6aabeb"
  },
    {
    "book_title": "Go Set a Watchman",
    "page_count": 278,
    "publish_date": "2015-07-14",
    "price": 27.99,
    "description": "Originally written in the mid-1950s, Go Set a Watchman was the novel Harper Lee first submitted to her publishers before To Kill a Mockingbird. It features many of the characters from the latter novel some twenty years later.",
    "inventory_count": 82,
    "isbn": "9780062409850",
    "author_id": "a98359d9-0d50-469e-9c98-2557d43f9b9c"
  },
  {
    "book_title": "Fahrenheit 451",
    "page_count": 158,
    "publish_date": "1953-10-19",
    "price": 15.99,
    "description": "A dystopian novel by American writer Ray Bradbury, about a future American society where books are outlawed and 'firemen' burn any that are found. The novel presents a future American society where books are outlawed and 'firemen' burn any that are found.",
    "inventory_count": 90,
    "isbn": "9781451673319",
    "author_id": "ba6835fe-babb-40f4-ab70-9cb04f9efc88"
  },
  {
    "book_title": "The War of the Worlds",
    "page_count": 192,
    "publish_date": "1898-01-01",
    "price": 8.99,
    "description": "An early science fiction work by H.G. Wells that describes an invasion of late Victorian England by Martians equipped with advanced weaponry. It is a seminal depiction of an alien invasion of Earth.",
    "inventory_count": 76,
    "isbn": "9780486295060",
    "author_id": "8c87a0c5-c01e-470f-b256-5776ab33dd96"
  },
  {
    "book_title": "The Tell-Tale Heart and Other Writings",
    "page_count": 448,
    "publish_date": "1982-10-01",
    "price": 6.95,
    "description": "A collection of Poe's most famous tales and poems, featuring 'The Tell-Tale Heart,' 'The Fall of the House of Usher,' 'The Cask of Amontillado,' and others. These tales explore themes of death, decay, and madness.",
    "inventory_count": 65,
    "isbn": "9780553212280",
    "author_id": "eba08f6a-63ae-4808-a778-479ffc4fbb8b"
  },
  {
    "book_title": "Selected Poems of Emily Dickinson",
    "page_count": 256,
    "publish_date": "2000-01-01",
    "price": 12.00,
    "description": "Emily Dickinson's poetry is a profound and largely idiosyncratic exploration of the mysteries of life, death, and nature. This selection includes some of her most famous poems, providing a good introduction to her work.",
    "inventory_count": 50,
    "isbn": "9780486411071",
    "author_id": "84b7e973-ece3-4ce3-82ac-34375a69993d"
  },
    {
    "book_title": "The Weary Blues",
    "page_count": 104,
    "publish_date": "1926-01-01",
    "price": 12.00,
    "description": "Hughes's first book of poetry, 'The Weary Blues,' describes the blues as both a major influence on his poetry and a major theme of his work.",
    "inventory_count": 50,
    "isbn": "9780486454481",
    "author_id": "ae029772-9302-4516-89ba-18dc518b7ae1"
  },
  {
    "book_title": "The Collected Poems of Langston Hughes",
    "page_count": 736,
    "publish_date": "1994-10-31",
    "price": 22.00,
    "description": "This collection presents 860 poems written by Hughes, one of the leading voices of the Harlem Renaissance.",
    "inventory_count": 80,
    "isbn": "9780679764083",
    "author_id": "ae029772-9302-4516-89ba-18dc518b7ae1"
  },
  {
    "book_title": "The Bell Jar",
    "page_count": 288,
    "publish_date": "1963-01-14",
    "price": 17.00,
    "description": "Plath's semi-autobiographical novel, which details the descent of Esther Greenwood, a young woman moving to New York City, into mental illness.",
    "inventory_count": 90,
    "isbn": "9780060837020",
    "author_id": "7989698a-1c58-400f-9a2c-3b2ce6a07f15"
  },
  {
    "book_title": "Brave New World",
    "page_count": 311,
    "publish_date": "1932-01-01",
    "price": 15.99,
    "description": "Huxley's masterpiece and arguably one of the most prescient dystopian works of the 20th century, imagining a future with a rigidly controlled society.",
    "inventory_count": 70,
    "isbn": "9780060850524",
    "author_id": "54de300c-c508-4e55-ba71-e38df42cc218"
  },
  {
    "book_title": "Moby-Dick",
    "page_count": 752,
    "publish_date": "1851-10-18",
    "price": 18.00,
    "description": "Melville's epic tale of obsession and revenge on the high seas, as Captain Ahab hunts the white whale, Moby-Dick, who maimed him.",
    "inventory_count": 85,
    "isbn": "9780142437247",
    "author_id": "de777e19-98bd-4da0-af06-653de1c60549"
  },
  {
    "book_title": "Little Women",
    "page_count": 449,
    "publish_date": "1868-09-30",
    "price": 12.95,
    "description": "Alcott's beloved novel follows the lives of the four March sisters—Meg, Jo, Beth, and Amy—and their journey from childhood to womanhood.",
    "inventory_count": 75,
    "isbn": "9780147514011",
    "author_id": "2246b53e-366a-4670-a137-5918f55f480b"
  },
    {
    "book_title": "The Picture of Dorian Gray",
    "page_count": 224,
    "publish_date": "1890-06-20",
    "price": 10.99,
    "description": "Oscar Wilde's only novel, it tells the story of a young man named Dorian Gray, who becomes the subject of a painting. As he seeks a life of pleasure and indulgence, he discovers that his portrait ages, reflecting the moral corruption of his choices, while he remains outwardly unchanged.",
    "inventory_count": 80,
    "isbn": "9780141439570",
    "author_id": "ab94b9de-2d6b-4c20-a024-d80d829b7887"
  },
  {
    "book_title": "The Importance of Being Earnest",
    "page_count": 76,
    "publish_date": "1895-02-14",
    "price": 6.95,
    "description": "A farcical comedy in which the protagonists maintain fictitious personae to escape burdensome social obligations. Wilde's most enduringly popular play.",
    "inventory_count": 95,
    "isbn": "9780486264784",
    "author_id": "ab94b9de-2d6b-4c20-a024-d80d829b7887"
  },
  {
    "book_title": "The Adventures of Sherlock Holmes",
    "page_count": 307,
    "publish_date": "1892-10-14",
    "price": 12.99,
    "description": "A collection of twelve short stories featuring Conan Doyle's legendary detective, Sherlock Holmes, and his loyal assistant Dr. Watson, as they solve mysteries in late 19th-century London.",
    "inventory_count": 70,
    "isbn": "9780755334507",
    "author_id": "fc2a1880-41f4-44f6-8937-472995f0f884"
  },
  {
    "book_title": "The Grapes of Wrath",
    "page_count": 464,
    "publish_date": "1939-04-14",
    "price": 14.00,
    "description": "John Steinbeck's epic novel of the Great Depression follows the Joad family as they're driven from their Oklahoma home and journey to California in search of work and a better life.",
    "inventory_count": 85,
    "isbn": "9780143039433",
    "author_id": "fa4fc70b-9594-461c-b967-a58f58ff8ded"
  },
  {
    "book_title": "The Great Gatsby",
    "page_count": 180,
    "publish_date": "1925-04-10",
    "price": 15.00,
    "description": "F. Scott Fitzgerald's masterpiece, a tragic love story set in the roaring twenties, which explores themes of decadence, idealism, resistance to change, social upheaval, and excess.",
    "inventory_count": 90,
    "isbn": "9780743273565",
    "author_id": "873ac726-d4ee-42e6-a0c7-fabc4494d0b2"
  },
  {
    "book_title": "American Gods",
    "page_count": 465,
    "publish_date": "2001-06-19",
    "price": 19.99,
    "description": "Neil Gaiman's novel blends Americana, fantasy, and various strands of ancient and modern mythology, all centering on the mysterious and taciturn Shadow.",
    "inventory_count": 88,
    "isbn": "9780062572233",
    "author_id": "e126fdfb-6d08-4f72-98fc-900d9ff62890"
  },
    {
    "book_title": "Do Androids Dream of Electric Sheep?",
    "page_count": 210,
    "publish_date": "1968-03-01",
    "price": 14.99,
    "description": "This novel, set in a post-apocalyptic San Francisco, follows Rick Deckard, a bounty hunter tasked with 'retiring' rogue androids. It explores themes of what it means to be human and the nature of humanity.",
    "inventory_count": 80,
    "isbn": "9780345404473",
    "author_id": "665f841e-75e9-44bb-9cb8-ca78752b4b78"
  },
  {
    "book_title": "The Man in the High Castle",
    "page_count": 274,
    "publish_date": "1962-01-01",
    "price": 13.95,
    "description": "An alternate history novel set in a world where the Axis powers won World War II. The story follows several characters living in the 1960s United States, now divided between Japan and Nazi Germany.",
    "inventory_count": 65,
    "isbn": "9780547572482",
    "author_id": "665f841e-75e9-44bb-9cb8-ca78752b4b78"
  },
  {
    "book_title": "The Handmaid's Tale",
    "page_count": 311,
    "publish_date": "1985-04-01",
    "price": 15.95,
    "description": "In a dystopian future, where a totalitarian regime enforces subservient roles on all women, Offred navigates the dangers of her reality with strength and cunning.",
    "inventory_count": 90,
    "isbn": "9780385490818",
    "author_id": "876dcb7c-c4ab-4f78-bef2-fb8a00980358"
  },
  {
    "book_title": "Oryx and Crake",
    "page_count": 400,
    "publish_date": "2003-05-06",
    "price": 16.95,
    "description": "Atwood's speculative fiction masterpiece, exploring genetic engineering and its impacts on humanity through the eyes of its protagonist, Snowman.",
    "inventory_count": 75,
    "isbn": "9780385503853",
    "author_id": "876dcb7c-c4ab-4f78-bef2-fb8a00980358"
  },
  {
    "book_title": "My Name Is Red",
    "page_count": 432,
    "publish_date": "1998-01-01",
    "price": 17.00,
    "description": "Set in late 16th century Istanbul, Pamuk's novel weaves a tale of intrigue and romance, centered around the Ottoman Empire's illustrious miniature artists.",
    "inventory_count": 82,
    "isbn": "9780375706851",
    "author_id": "e06c4323-387e-4ebb-8161-292026077b46"
  },
  {
    "book_title": "The House of the Spirits",
    "page_count": 448,
    "publish_date": "1982-10-01",
    "price": 18.00,
    "description": "Allende's debut novel, combining magical realism with political and social insight, it tells the epic story of the Trueba family over several generations.",
    "inventory_count": 70,
    "isbn": "9781501117015",
    "author_id": "ee888d45-4f8c-4818-83d8-83e0db69597f"
  },
  {
    "book_title": "Never Let Me Go",
    "page_count": 288,
    "publish_date": "2005-04-05",
    "price": 16.00,
    "description": "Ishiguro's haunting story of Kathy, Tommy, and Ruth, and their journey of memories and the truth about their seemingly idyllic school, Hailsham, which hides a dark secret.",
    "inventory_count": 88,
    "isbn": "9781400078774",
    "author_id": "24bad126-0f71-4de7-b639-289fb5fa4c27"
  },
  
]

# books_data = [
#     {
#         "book_title": "1984",
#         "page_count": 328,
#         "publish_date": "1949-06-08",
#         "price": 19.84,
#         "description": "A dystopian novel by English novelist George Orwell.",
#         "inventory_count": 120,
#         "isbn": "978-0451524935",
#         "author_id": 1
#     },
#     {
#         "book_title": "Animal Farm",
#         "page_count": 112,
#         "publish_date": "1945-08-17",
#         "price": 12.99,
#         "description": "A fairy story by George Orwell, portraying a revolution by farm animals against humans.",
#         "inventory_count": 100,
#         "isbn": "978-0451526342",
#         "author_id": 1
#     },
#     {
#         "book_title": "To the Lighthouse",
#         "page_count": 209,
#         "publish_date": "1927-05-05",
#         "price": 15.20,
#         "description": "The Ramsays and their eight children vacation with an assortment of scholarly and artistic houseguests by the sea.",
#         "inventory_count": 85,
#         "isbn": "978-0156907392",
#         "author_id": 2
#     },
#     {
#         "book_title": "Mrs Dalloway",
#         "page_count": 194,
#         "publish_date": "1925-05-14",
#         "price": 13.95,
#         "description": "The novel details a day in the life of Clarissa Dalloway, a fictional high-society woman in post–First World War England.",
#         "inventory_count": 75,
#         "isbn": "978-0156628709",
#         "author_id": 2
#     },
#     {
#         "book_title": "The Old Man and The Sea",
#         "page_count": 128,
#         "publish_date": "1952-09-01",
#         "price": 15,
#         "description": "The story of an old Cuban fisherman and his supreme ordeal: a relentless, agonizing battle with a giant marlin far out in the Gulf Stream.",
#         "inventory_count": 100,
#         "isbn": "978-0684801223",
#         "author_id": 3
#     },
#     {
#         "book_title": "A Farewell to Arms",
#         "page_count": 332,
#         "publish_date": "1929-10-28",
#         "price": 17,
#         "description": "A novel written by Ernest Hemingway set during the Italian campaign of World War I.",
#         "inventory_count": 80,
#         "isbn": "978-0684801469",
#         "author_id": 3
#     },
#     {
#         "book_title": "Ulysses",
#         "page_count": 730,
#         "publish_date": "1922-02-02",
#         "price": 24.95,
#         "description": "The novel imitates registers of centuries of English literature and is highly allusive.",
#         "inventory_count": 60,
#         "isbn": "978-0679722762",
#         "author_id": 4
#     },
#     {
#         "book_title": "Finnegans Wake",
#         "page_count": 628,
#         "publish_date": "1939-05-04",
#         "price": 22.95,
#         "description": "A work of fiction by Irish writer James Joyce, significant for its experimental style.",
#         "inventory_count": 40,
#         "isbn": "978-0141181264",
#         "author_id": 4
#     },
#     {
#         "book_title": "Wuthering Heights",
#         "page_count": 464,
#         "publish_date": "1847-12-01",
#         "price": 14.99,
#         "description": "A novel by Emily Bronte, it follows the life of Heathcliff, a mysterious gypsy-like person.",
#         "inventory_count": 50,
#         "isbn": "978-0553212587",
#         "author_id": 5
#     },
#     {
#         "book_title": "Pride and Prejudice",
#         "page_count": 279,
#         "publish_date": "1813-01-28",
#         "price": 9.99,
#         "description": "A romantic novel of manners written by Jane Austen.",
#         "inventory_count": 120,
#         "isbn": "978-1503290563",
#         "author_id": 6
#     },
#         {
#         "book_title": "Emma",
#         "page_count": 368,
#         "publish_date": "1815-12-23",
#         "price": 12.99,
#         "description": "A novel about youthful hubris and romantic misunderstandings. It is set in the fictional country village of Highbury and the surrounding estates of Hartfield, Randalls, and Donwell Abbey.",
#         "inventory_count": 70,
#         "isbn": "978-0141439587",
#         "author_id": 6
#     },
#     {
#         "book_title": "Great Expectations",
#         "page_count": 544,
#         "publish_date": "1861-08-01",
#         "price": 10.99,
#         "description": "The novel, written by Charles Dickens, is a bildungsroman, a coming-of-age story, and it is a classic work of Victorian literature.",
#         "inventory_count": 85,
#         "isbn": "978-0141439563",
#         "author_id": 7
#     },
#     {
#         "book_title": "Oliver Twist",
#         "page_count": 368,
#         "publish_date": "1838-02-01",
#         "price": 11.99,
#         "description": "The novel tells the story of an orphan boy and his experiences with crime and hardship in London.",
#         "inventory_count": 65,
#         "isbn": "978-0486424538",
#         "author_id": 7
#     },
#     {
#         "book_title": "Adventures of Huckleberry Finn",
#         "page_count": 224,
#         "publish_date": "1884-12-10",
#         "price": 9.99,
#         "description": "A novel by Mark Twain, it is commonly named among the Great American Novels. The work is among the first in major American literature to be written throughout in vernacular English.",
#         "inventory_count": 90,
#         "isbn": "978-0486449900",
#         "author_id": 8
#     },
#     {
#         "book_title": "The Adventures of Tom Sawyer",
#         "page_count": 184,
#         "publish_date": "1876-06-01",
#         "price": 8.99,
#         "description": "The novel is set in the 1840s in the town of St. Petersburg, which is based on Hannibal, Missouri where Twain lived as a boy.",
#         "inventory_count": 80,
#         "isbn": "978-0486400778",
#         "author_id": 8
#     },
#     {
#         "book_title": "To Kill a Mockingbird",
#         "page_count": 281,
#         "publish_date": "1960-07-11",
#         "price": 14.99,
#         "description": "The novel is renowned for its warmth and humor, despite dealing with serious issues of rape and racial inequality.",
#         "inventory_count": 120,
#         "isbn": "978-0446310789",
#         "author_id": 9
#     },
#     {
#         "book_title": "Go Set a Watchman",
#         "page_count": 278,
#         "publish_date": "2015-07-14",
#         "price": 15.99,
#         "description": "Written in the mid-1950s, the novel was published by Harper Lee in 2015, as a follow-up to To Kill a Mockingbird.",
#         "inventory_count": 70,
#         "isbn": "978-0062409850",
#         "author_id": 9
#     },
#     {
#         "book_title": "The Catcher in the Rye",
#         "page_count": 277,
#         "publish_date": "1951-07-16",
#         "price": 8.99,
#         "description": "The novel's protagonist, Holden Caulfield, has become an icon for teenage rebellion and angst.",
#         "inventory_count": 95,
#         "isbn": "978-7543321724",
#         "author_id": 10
#     },
#     {
#         "book_title": "Nine Stories",
#         "page_count": 198,
#         "publish_date": "1953-04-06",
#         "price": 10.99,
#         "description": "A collection of short stories by J.D. Salinger. It includes two of his most famous short stories, 'A Perfect Day for Bananafish' and 'For Esmé – with Love and Squalor'.",
#         "inventory_count": 75,
#         "isbn": "978-0316769495",
#         "author_id": 10
#     },
#     {
#         "book_title": "Franny and Zooey",
#         "page_count": 201,
#         "publish_date": "1961-09-12",
#         "price": 12.99,
#         "description": "The book comprises his short story 'Franny' and novella 'Zooey', both of which revolve around the two youngest members of the Glass family.",
#         "inventory_count": 65,
#         "isbn": "978-0316769495",
#         "author_id": 10
#     }
# ]
