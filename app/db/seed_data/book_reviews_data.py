reviews_data = [
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '94214347-e2c1-4fa4-872f-2b02dfaccfef', 'book_rating': 5, 'book_review': "The Alchemist is an incredible journey of self-discovery and following one's dreams. Highly recommend it!", 'short_review': 'Incredible journey!', 'id': 'c755018d-e4b9-4e77-8c83-e6b0ca99354d'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '4e693a90-d582-421b-afbf-a4babf10a68e', 'book_rating': 3, 'book_review': 'Pride and Prejudice is a classic romance with memorable characters. However, I found some parts to be a bit slow.', 'short_review': 'Classic romance.', 'id': '8adb6034-e91b-40b5-a2f4-f854d0f4327d'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '94214347-e2c1-4fa4-872f-2b02dfaccfef', 'book_rating': 4, 'book_review': "The Alchemist is a thought-provoking book that teaches valuable life lessons. It's definitely worth reading.", 'short_review': 'Thought-provoking!', 'id': 'e6d8806a-bdf2-4c0e-ae6a-557cb8f4fc53'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '4e693a90-d582-421b-afbf-a4babf10a68e', 'book_rating': 2, 'book_review': 'Pride and Prejudice was not my cup of tea. I found it to be overly dramatic and lacking depth in character development.', 'short_review': 'Not my cup of tea.', 'id': '2e5f373e-f46e-4f59-a7e2-d7f0f3800ebc'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '94214347-e2c1-4fa4-872f-2b02dfaccfef', 'book_rating': 5, 'book_review': "The Alchemist is a masterpiece! It's beautifully written and deeply moving. A must-read for everyone!", 'short_review': 'A masterpiece!', 'id': 'b370d54d-86a5-4a06-b801-79a4da29c85e'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '4e693a90-d582-421b-afbf-a4babf10a68e', 'book_rating': 4, 'book_review': 'Pride and Prejudice is a charming novel with witty dialogue and engaging characters. I thoroughly enjoyed reading it.', 'short_review': 'Charming novel.', 'id': '1989cb7e-62eb-4e91-8b45-c5b740bf2036'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '94214347-e2c1-4fa4-872f-2b02dfaccfef', 'book_rating': 3, 'book_review': 'The Alchemist has some good moments, but overall, I found it to be a bit too preachy for my taste.', 'short_review': 'Bit too preachy.', 'id': '171b5ddc-7c09-44b0-aecb-c8856d421a6f'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '4e693a90-d582-421b-afbf-a4babf10a68e', 'book_rating': 5, 'book_review': 'Pride and Prejudice is a timeless classic that never fails to charm readers with its wit and romance. A must-read for any book lover!', 'short_review': 'Timeless classic!', 'id': '326b9835-a9a8-4780-9844-23492025e3e6'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '5868f357-1e51-4383-a603-b21dd5881b18', 'book_rating': 4, 'book_review': 'The Adventures of Huckleberry Finn is a classic adventure tale with memorable characters and exciting escapades. Highly recommend it!', 'short_review': 'Classic adventure!', 'id': '53299f33-8fd8-4a38-a5f7-f41af71ee56c'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': 'cb16b8cd-82b2-4489-9a7f-7e085051a001', 'book_rating': 3, 'book_review': 'Mrs. Dalloway is a thought-provoking novel that explores the complexities of human consciousness. Worth reading for its literary merit.', 'short_review': 'Thought-provoking.', 'id': 'c33e16ec-d836-4593-bf22-92c523bb5323'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '5868f357-1e51-4383-a603-b21dd5881b18', 'book_rating': 5, 'book_review': "The Adventures of Huckleberry Finn is an absolute delight to read! Twain's storytelling prowess shines through every page.", 'short_review': 'Absolute delight!', 'id': '01c3c7c6-9910-4fe6-a801-c764d56b341b'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': 'cb16b8cd-82b2-4489-9a7f-7e085051a001', 'book_rating': 2, 'book_review': 'Mrs. Dalloway was not my cup of tea. I found the stream of consciousness style confusing and hard to follow.', 'short_review': 'Not my cup of tea.', 'id': '597206f7-7b70-4501-b63d-3264b48b74ae'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '5868f357-1e51-4383-a603-b21dd5881b18', 'book_rating': 4, 'book_review': "The Adventures of Huckleberry Finn is a timeless classic that never fails to entertain. Twain's wit and humor make it a joy to read.", 'short_review': 'Timeless classic!', 'id': 'e8c18b11-328a-42fe-98f3-59540f5c3d78'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'cb16b8cd-82b2-4489-9a7f-7e085051a001', 'book_rating': 5, 'book_review': "Mrs. Dalloway is a masterpiece of modernist literature. Woolf's portrayal of consciousness is both innovative and captivating.", 'short_review': 'Modernist masterpiece!', 'id': '0b140bbc-add7-4557-aa62-cf85e73cf77d'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '5868f357-1e51-4383-a603-b21dd5881b18', 'book_rating': 3, 'book_review': 'The Adventures of Huckleberry Finn was a decent read. While some parts were engaging, others felt slow and dragged on.', 'short_review': 'Decent read.', 'id': '41517285-898b-4599-8a83-88abfc84c681'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': 'cb16b8cd-82b2-4489-9a7f-7e085051a001', 'book_rating': 4, 'book_review': "Mrs. Dalloway is a beautifully written novel that offers profound insights into the human psyche. Woolf's prose is exquisite.", 'short_review': 'Beautifully written.', 'id': '6fb38836-da13-4f02-924a-a342e5802334'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '81b45f95-dd8b-40b9-a4ef-3754963d5f7a', 'book_rating': 5, 'book_review': "Anna Karenina is a timeless masterpiece that delves deep into the complexities of love and society. Tolstoy's characters are richly developed, and the narrative is beautifully crafted.", 'short_review': 'Timeless masterpiece!', 'id': 'afd6e98a-c100-4be9-85e1-85135e45c172'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '6e515ee5-0529-4013-ad25-5c3c5f4d79b1', 'book_rating': 3, 'book_review': 'Warrior of the Light offers some inspiring insights, but overall, I found it to be a bit repetitive. The message is uplifting, but it could have been conveyed more effectively.', 'short_review': 'Inspiring but repetitive.', 'id': 'd58de802-68f9-489b-b010-d6b4ca222ed3'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '81b45f95-dd8b-40b9-a4ef-3754963d5f7a', 'book_rating': 4, 'book_review': "Anna Karenina is a powerful exploration of human emotions and desires. Tolstoy's storytelling prowess shines through every page, making it a compelling read.", 'short_review': 'Powerful exploration.', 'id': 'b01ac4e5-6a00-42f5-8c72-f85a9aa7f0d2'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '6e515ee5-0529-4013-ad25-5c3c5f4d79b1', 'book_rating': 2, 'book_review': 'Warrior of the Light was a disappointment for me. I expected more profound wisdom, but it felt shallow and clich�. Not worth the hype.', 'short_review': 'Disappointing.', 'id': '489e818d-b1ac-4a2d-861a-a130039750bd'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '81b45f95-dd8b-40b9-a4ef-3754963d5f7a', 'book_rating': 5, 'book_review': "Anna Karenina is an absolute gem of literature! Tolstoy's ability to capture the human condition is unparalleled. A must-read for any book lover.", 'short_review': 'Absolute gem!', 'id': 'efc0f0c0-119c-49ac-9646-f72d691dadae'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '6e515ee5-0529-4013-ad25-5c3c5f4d79b1', 'book_rating': 4, 'book_review': "Warrior of the Light provides some valuable life lessons and motivational quotes. It's a quick read that can uplift your spirits when needed.", 'short_review': 'Valuable life lessons.', 'id': '99c197b9-3539-4239-8938-73503335ee65'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '81b45f95-dd8b-40b9-a4ef-3754963d5f7a', 'book_rating': 3, 'book_review': 'Anna Karenina was a bit of a mixed bag for me. While I appreciated the depth of the characters, I found the plot to be overly complex and meandering.', 'short_review': 'Mixed bag.', 'id': '22334e5a-5654-41b0-9f2b-8321a9187f9e'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '6e515ee5-0529-4013-ad25-5c3c5f4d79b1', 'book_rating': 5, 'book_review': 'Warrior of the Light is a beacon of hope in the darkness. Its messages of perseverance and courage are exactly what I needed to hear. Highly recommend it!', 'short_review': 'Beacon of hope!', 'id': 'b13375d5-71ed-4368-9014-28a057aca4bb'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': 'efdd1fbe-91bb-4e26-9709-30c863b41cec', 'book_rating': 4, 'book_review': "Emma is a delightful read with charming characters and witty dialogue. Austen's writing style is captivating, making it a classic.", 'short_review': 'Delightful read!', 'id': 'e9909fb2-e828-4c26-92d1-b2b75953b251'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': 'ae30fc90-3b04-48b1-b3a9-eedabe83457c', 'book_rating': 3, 'book_review': "Life on the Mississippi provides an interesting glimpse into the life along the river. Twain's anecdotes are amusing, but the narrative feels a bit disjointed.", 'short_review': 'Interesting glimpse.', 'id': '17506e47-69a0-4c8e-96d5-798ca4812080'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': 'efdd1fbe-91bb-4e26-9709-30c863b41cec', 'book_rating': 5, 'book_review': "Emma is an absolute masterpiece! Austen's portrayal of society and romance is unparalleled. A must-read for any literature enthusiast.", 'short_review': 'Absolute masterpiece!', 'id': 'f720c0d9-2f85-4370-a9ae-6e7c59a9eff8'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': 'ae30fc90-3b04-48b1-b3a9-eedabe83457c', 'book_rating': 2, 'book_review': 'Life on the Mississippi was a disappointment for me. I expected more engaging storytelling, but it felt tedious and overly descriptive.', 'short_review': 'Disappointing.', 'id': 'de6f21ce-6951-436f-b5c5-18246df229df'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'efdd1fbe-91bb-4e26-9709-30c863b41cec', 'book_rating': 4, 'book_review': "Emma is a classic novel with timeless themes of love, friendship, and self-discovery. Austen's characters are vividly drawn, and the plot is engaging.", 'short_review': 'Timeless themes.', 'id': 'b7e42116-c20c-4068-90de-b72370974ef1'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'ae30fc90-3b04-48b1-b3a9-eedabe83457c', 'book_rating': 4, 'book_review': "Life on the Mississippi offers a fascinating look at the river and the people who inhabit its shores. Twain's wit shines through, making it an enjoyable read.", 'short_review': 'Fascinating look.', 'id': 'feff001d-bdc6-4082-8ac9-a830b3d2530a'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'efdd1fbe-91bb-4e26-9709-30c863b41cec', 'book_rating': 3, 'book_review': "Emma was an okay read for me. While I appreciated Austen's wit, I found some parts to be a bit slow-paced.", 'short_review': 'Okay read.', 'id': 'a01f4eda-d8b4-4b60-b01f-1f68ae26656e'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': 'ae30fc90-3b04-48b1-b3a9-eedabe83457c', 'book_rating': 5, 'book_review': "Life on the Mississippi is a fascinating blend of history, humor, and adventure. Twain's observations are sharp and his storytelling is engaging. Highly recommend it!", 'short_review': 'Fascinating blend!', 'id': '90d90825-da03-45bc-b47f-21ad0cd5685c'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '4bad32a8-6fba-4f3e-bff5-68d675149a9b', 'book_rating': 5, 'book_review': "Orlando is a mesmerizing tale of transformation and identity. Woolf's prose is enchanting, and the exploration of gender and time is thought-provoking.", 'short_review': 'Mesmerizing tale!', 'id': '8249fc66-3552-495c-b008-10bc226ec74e'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '1b1f18d6-05c6-443d-94bf-c42595b16506', 'book_rating': 4, 'book_review': "The Death of Ivan Ilyich is a profound reflection on life and mortality. Tolstoy's examination of existential themes is both haunting and enlightening.", 'short_review': 'Profound reflection.', 'id': '45e8b346-1c53-4a55-8f8a-407e6559c3dc'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '4bad32a8-6fba-4f3e-bff5-68d675149a9b', 'book_rating': 3, 'book_review': 'Orlando is an interesting blend of fantasy and biography. While the concept is intriguing, I found the execution to be somewhat disjointed.', 'short_review': 'Interesting blend.', 'id': '31832964-82d1-4947-9fed-ec167a5f1fa3'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '1b1f18d6-05c6-443d-94bf-c42595b16506', 'book_rating': 2, 'book_review': "The Death of Ivan Ilyich left me feeling unsatisfied. The protagonist's journey felt shallow, and the narrative lacked depth.", 'short_review': 'Unsatisfying.', 'id': 'ab91d6ec-7b54-44fe-a0d2-1f0219f2e2b8'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '4bad32a8-6fba-4f3e-bff5-68d675149a9b', 'book_rating': 5, 'book_review': "Orlando is a masterpiece of modernist literature. Woolf's exploration of gender fluidity and historical narrative is groundbreaking.", 'short_review': 'Masterpiece!', 'id': 'e80a88b1-30ce-4f8a-8e0d-4d085bc4b8aa'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '1b1f18d6-05c6-443d-94bf-c42595b16506', 'book_rating': 4, 'book_review': "The Death of Ivan Ilyich offers a profound meditation on the nature of life and death. Tolstoy's writing is deeply introspective and emotionally resonant.", 'short_review': 'Profound meditation.', 'id': 'a8ce610a-180c-446b-a3d4-d6880583909b'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '4bad32a8-6fba-4f3e-bff5-68d675149a9b', 'book_rating': 3, 'book_review': 'Orlando is an ambitious novel with an interesting premise. However, I found some parts to be tedious and overly descriptive.', 'short_review': 'Ambitious but tedious.', 'id': '79c46314-d59d-4b30-9c81-906bec115ee9'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '1b1f18d6-05c6-443d-94bf-c42595b16506', 'book_rating': 5, 'book_review': "The Death of Ivan Ilyich is a haunting portrayal of mortality and the human condition. Tolstoy's prose is profound and poignant, leaving a lasting impact.", 'short_review': 'Haunting portrayal.', 'id': '0b355d04-a595-4d6e-9586-a7501dc04ecf'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': 'd0abc5bc-8dc2-40a2-8670-a57bd1f0ca74', 'book_rating': 5, 'book_review': "The Brothers Karamazov is a masterpiece of Russian literature. Dostoevsky's exploration of morality, faith, and family dynamics is profound and thought-provoking.", 'short_review': 'Masterpiece!', 'id': 'b2de357e-35c2-4c68-a603-6025b708230c'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '3a9423c9-5500-468d-ad74-871ce83dc158', 'book_rating': 4, 'book_review': "Notes from Underground is a compelling and introspective work. Dostoevsky's portrayal of the human psyche is both unsettling and captivating.", 'short_review': 'Compelling read!', 'id': 'db822deb-97cb-404b-8c1f-00145260094e'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': 'd0abc5bc-8dc2-40a2-8670-a57bd1f0ca74', 'book_rating': 3, 'book_review': 'The Brothers Karamazov is a challenging read. While the philosophical themes are intriguing, the narrative can be dense and difficult to follow.', 'short_review': 'Challenging read.', 'id': 'ee7b9b37-3a43-4277-af1f-a979bad3c618'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '3a9423c9-5500-468d-ad74-871ce83dc158', 'book_rating': 2, 'book_review': "Notes from Underground left me feeling disappointed. The protagonist's ramblings felt tedious and pretentious.", 'short_review': 'Disappointing.', 'id': '2314e8d2-ea82-48e4-831c-1db876924f87'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'd0abc5bc-8dc2-40a2-8670-a57bd1f0ca74', 'book_rating': 5, 'book_review': "The Brothers Karamazov is a profound exploration of the human condition. Dostoevsky's characters are vividly drawn, and the plot is rich with philosophical depth.", 'short_review': 'Profound exploration.', 'id': 'ca8c350a-d1b2-4b64-9389-0183da7a31c9'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '3a9423c9-5500-468d-ad74-871ce83dc158', 'book_rating': 4, 'book_review': "Notes from Underground is a dark and introspective novel. Dostoevsky's examination of alienation and existential angst is both unsettling and enlightening.", 'short_review': 'Dark and introspective.', 'id': 'fba12e53-6651-4c15-82c1-b74fd2a6e996'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'd0abc5bc-8dc2-40a2-8670-a57bd1f0ca74', 'book_rating': 3, 'book_review': 'The Brothers Karamazov is a classic work, but I found some parts to be overly philosophical and verbose.', 'short_review': 'Classic but verbose.', 'id': '44a0e467-49ba-454c-8114-3c619e58cf44'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '3a9423c9-5500-468d-ad74-871ce83dc158', 'book_rating': 5, 'book_review': "Notes from Underground is a compelling portrayal of the human psyche. Dostoevsky's insights into the complexities of human nature are unparalleled.", 'short_review': 'Compelling portrayal.', 'id': '564f71ac-de62-4feb-87e2-3c5139f6bfc2'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '63970168-6e81-4cf4-b388-1052bacf712e', 'book_rating': 4, 'book_review': "For Whom the Bell Tolls is a powerful and evocative novel set during the Spanish Civil War. Hemingway's portrayal of the characters' struggles and the brutality of war is gripping.", 'short_review': 'Powerful and gripping.', 'id': '63d10e02-bb86-4731-b346-007b913b2caa'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': 'bf0350e9-25d4-42bb-8c68-ec8f243e1755', 'book_rating': 5, 'book_review': "A Farewell to Arms is a timeless classic that explores the harsh realities of war and the complexities of love. Hemingway's prose is both beautiful and haunting.", 'short_review': 'Timeless classic!', 'id': 'f89c982f-b7dd-4035-81e1-d71827f29fd2'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '63970168-6e81-4cf4-b388-1052bacf712e', 'book_rating': 3, 'book_review': 'For Whom the Bell Tolls has its moments, but I found some parts to be slow-paced. The themes are important, but the execution could have been better.', 'short_review': 'Has its moments.', 'id': '79b48f3f-9f16-4d90-adcc-54c275ae1b20'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': 'bf0350e9-25d4-42bb-8c68-ec8f243e1755', 'book_rating': 2, 'book_review': 'A Farewell to Arms left me disappointed. The plot felt predictable, and the characters lacked depth.', 'short_review': 'Disappointing.', 'id': '17d45a11-ff5e-4192-87d4-5c7a8338e8cf'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '63970168-6e81-4cf4-b388-1052bacf712e', 'book_rating': 5, 'book_review': "For Whom the Bell Tolls is a masterfully written novel that captures the essence of wartime struggle and sacrifice. Hemingway's prose is both poignant and profound.", 'short_review': 'Masterfully written.', 'id': '7dc80cd4-79f6-4bd3-9007-efc2f12dc6f7'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'bf0350e9-25d4-42bb-8c68-ec8f243e1755', 'book_rating': 4, 'book_review': "A Farewell to Arms is a compelling narrative that beautifully captures the chaos and heartbreak of war. Hemingway's portrayal of love amidst adversity is deeply moving.", 'short_review': 'Compelling narrative.', 'id': 'bb65dc89-35f3-4d36-83b2-5c01eccb619f'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '63970168-6e81-4cf4-b388-1052bacf712e', 'book_rating': 3, 'book_review': 'For Whom the Bell Tolls is an important literary work, but I struggled to connect with the characters. The pacing felt uneven at times.', 'short_review': 'Important but uneven.', 'id': '9a0801db-aff9-4e5b-809f-4fe99fc3aa5f'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': 'bf0350e9-25d4-42bb-8c68-ec8f243e1755', 'book_rating': 4, 'book_review': "A Farewell to Arms is a poignant and heartbreaking tale of love and loss amidst the chaos of war. Hemingway's writing style is both powerful and restrained.", 'short_review': 'Poignant and heartbreaking.', 'id': '7eb23f98-85ce-402b-b203-588dde765e87'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': 'af368a43-b2b8-4e26-a947-51b2a7b09696', 'book_rating': 5, 'book_review': "The Hobbit is an enchanting tale filled with adventure and wonder. Tolkien's world-building is exceptional, and the characters are memorable.", 'short_review': 'Enchanting tale!', 'id': 'e4e3dbc4-7553-46e8-b51a-fe30b103f55f'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '4e73e36a-1496-4566-b39a-016b04a2b6c2', 'book_rating': 4, 'book_review': "Animal Farm is a thought-provoking allegory that offers insights into politics and human nature. Orwell's writing is concise yet impactful.", 'short_review': 'Thought-provoking.', 'id': 'a8d9c527-2da6-41e3-a45b-6bba18118fcd'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': 'af368a43-b2b8-4e26-a947-51b2a7b09696', 'book_rating': 3, 'book_review': "The Hobbit was enjoyable, but I found some parts to be slow-paced. Nonetheless, Tolkien's creativity shines through.", 'short_review': 'Enjoyable but slow-paced.', 'id': 'baaf0cc7-176b-4076-be4a-875cf26f1901'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '4e73e36a-1496-4566-b39a-016b04a2b6c2', 'book_rating': 2, 'book_review': 'Animal Farm disappointed me. While the allegory is clever, I found the execution lacking. The characters felt one-dimensional.', 'short_review': 'Disappointing execution.', 'id': '089ab597-46eb-4906-8ee2-1fa607a871ec'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'af368a43-b2b8-4e26-a947-51b2a7b09696', 'book_rating': 5, 'book_review': "The Hobbit is a timeless classic that appeals to readers of all ages. Tolkien's imagination transports you to a magical world filled with dragons, elves, and dwarves.", 'short_review': 'Timeless classic!', 'id': '5e1ed5aa-c444-483f-914e-c228e5a520a0'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '4e73e36a-1496-4566-b39a-016b04a2b6c2', 'book_rating': 4, 'book_review': "Animal Farm is a chilling critique of totalitarianism and corrupt leadership. Orwell's allegorical storytelling is both clever and unsettling.", 'short_review': 'Chilling critique.', 'id': '96099885-e2b0-431a-9da1-bfb32d5473bf'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'af368a43-b2b8-4e26-a947-51b2a7b09696', 'book_rating': 3, 'book_review': "The Hobbit is a classic adventure, but I found the pacing uneven at times. Nonetheless, Tolkien's world-building is impressive.", 'short_review': 'Classic adventure.', 'id': '11b31a5b-55f7-4f05-8c58-c63417231372'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '4e73e36a-1496-4566-b39a-016b04a2b6c2', 'book_rating': 5, 'book_review': "Animal Farm is a brilliant satire that remains relevant today. Orwell's writing is incisive, and the allegory is executed flawlessly.", 'short_review': 'Brilliant satire!', 'id': '8455df28-73b5-4036-b7e1-4290a085da3f'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '79e3a677-fb5d-4fd9-80be-ac66ab17196e', 'book_rating': 4, 'book_review': "The Sound and the Fury is a complex and challenging read, but it rewards those who persevere. Faulkner's writing style may be difficult to follow at times, but the depth of the characters and themes makes it worthwhile.", 'short_review': 'Complex and rewarding.', 'id': '27d35782-ccd3-479c-82fd-d42074f066b3'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '620cdcdc-1f5b-4822-9612-8d82467e9c20', 'book_rating': 5, 'book_review': "Murder on the Orient Express is a thrilling mystery that keeps you guessing until the end. Agatha Christie's plot twists and intricate characters make it a masterpiece of detective fiction.", 'short_review': 'Thrilling mystery!', 'id': '682ae87f-209a-46af-88a2-1e7840387947'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '7fcf3d23-419c-454b-850f-1c07317caf8c', 'book_rating': 2, 'book_review': "Ulysses is an ambitious and experimental novel, but I found it excessively dense and convoluted. Joyce's stream-of-consciousness style made it difficult for me to connect with the story.", 'short_review': 'Ambitious but dense.', 'id': '032385b8-ae71-4be7-8e9c-b6dcc993cd59'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '79e3a677-fb5d-4fd9-80be-ac66ab17196e', 'book_rating': 3, 'book_review': 'The Sound and the Fury is a literary masterpiece with its intricate narrative structure and profound exploration of human consciousness. However, its non-linear storytelling may not be for everyone.', 'short_review': 'Literary masterpiece.', 'id': '124e302c-935a-485c-b173-8a65a37145a3'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '620cdcdc-1f5b-4822-9612-8d82467e9c20', 'book_rating': 4, 'book_review': "Murder on the Orient Express is a classic whodunit that keeps readers engaged from start to finish. Agatha Christie's plot twists are expertly crafted, making it a must-read for mystery enthusiasts.", 'short_review': 'Engaging whodunit.', 'id': 'a14cafe5-34b8-4236-bf6b-d1ed1d29c689'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '7fcf3d23-419c-454b-850f-1c07317caf8c', 'book_rating': 5, 'book_review': "Ulysses is a literary tour de force that pushes the boundaries of conventional storytelling. Joyce's innovative use of language and symbolism creates a rich and immersive reading experience.", 'short_review': 'Innovative storytelling.', 'id': '83efb705-5ff7-426f-aec6-fe0fb2b66a5f'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '79e3a677-fb5d-4fd9-80be-ac66ab17196e', 'book_rating': 3, 'book_review': "The Sound and the Fury is a challenging read due to its nonlinear narrative structure, but it offers profound insights into the human condition. Faulkner's writing style is both beautiful and bewildering.", 'short_review': 'Profound insights.', 'id': '5d7eb5e6-86ef-4ef1-b367-05a69b89bb1e'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '620cdcdc-1f5b-4822-9612-8d82467e9c20', 'book_rating': 4, 'book_review': "Murder on the Orient Express is a captivating mystery with a clever plot and well-developed characters. Agatha Christie's storytelling prowess shines through in this classic novel.", 'short_review': 'Captivating mystery.', 'id': '22e3e191-9e1a-4c05-a1bf-5e0bf0acbc39'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': 'b837fef5-40fb-474e-ba91-87c717c37544', 'book_rating': 4, 'book_review': "The Trial is a thought-provoking novel that explores themes of bureaucracy and existentialism. Kafka's writing style is captivating, although the story can be unsettling at times.", 'short_review': 'Thought-provoking.', 'id': '0ca950b8-4306-4efb-8a4a-7c2c9cc14292'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '5c6d507d-0b1f-494f-86b2-61f5a64e1fbe', 'book_rating': 5, 'book_review': "Beloved is a powerful and haunting novel that delves into the legacy of slavery and its impact on individuals and families. Morrison's prose is beautifully crafted, and the story stays with you long after reading.", 'short_review': 'Powerful and haunting.', 'id': '43a27e95-a3b3-4fb3-ba35-afb66d1e3850'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': 'cdd9ff82-fbbe-4473-9469-4e639ec6eaf5', 'book_rating': 3, 'book_review': 'One Hundred Years of Solitude is an ambitious novel with its intricate storytelling and magical realism. While some may find it enchanting, I struggled to connect with the multitude of characters and their interwoven stories.', 'short_review': 'Ambitious but challenging.', 'id': '1f7735cd-e5e7-495b-bece-9cf6601041b0'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': 'b837fef5-40fb-474e-ba91-87c717c37544', 'book_rating': 4, 'book_review': "The Trial is a surreal journey into the absurdity of modern society. Kafka's portrayal of bureaucracy and the individual's struggle against it is both unsettling and thought-provoking.", 'short_review': 'Surreal and thought-provoking.', 'id': 'a2fa20c8-eb57-4d4a-a780-4b69a4978aab'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '5c6d507d-0b1f-494f-86b2-61f5a64e1fbe', 'book_rating': 5, 'book_review': "Beloved is a masterful work of literature that confronts the horrors of slavery with raw honesty and empathy. Morrison's storytelling is deeply moving, making this a must-read for all.", 'short_review': 'Masterful and moving.', 'id': '3f3121d2-97b6-4421-ac61-b73201c71bb6'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'cdd9ff82-fbbe-4473-9469-4e639ec6eaf5', 'book_rating': 4, 'book_review': "One Hundred Years of Solitude is a mesmerizing tale that spans generations, blending reality with myth and magic. Garc�a M�rquez's prose is enchanting, although the nonlinear narrative may require patience.", 'short_review': 'Mesmerizing and enchanting.', 'id': '77219b52-71e7-4322-82ed-741d09d9f0b7'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'b837fef5-40fb-474e-ba91-87c717c37544', 'book_rating': 3, 'book_review': "The Trial offers a surreal exploration of the absurdity of the legal system. While Kafka's writing is compelling, the lack of resolution may frustrate some readers.", 'short_review': 'Surreal exploration.', 'id': 'acb8519f-3916-4c7f-8363-40552285bc7a'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '5c6d507d-0b1f-494f-86b2-61f5a64e1fbe', 'book_rating': 4, 'book_review': "Beloved is a haunting and evocative novel that captures the pain and resilience of its characters. Morrison's prose is lyrical, and the story stays with you long after finishing.", 'short_review': 'Haunting and evocative.', 'id': '4faec2d1-29a7-4a74-a477-a5fb4ce4bfe5'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '206b9fe4-f7c1-4549-9641-c025ce74cf06', 'book_rating': 4, 'book_review': "Norwegian Wood is a beautifully written novel that explores themes of love, loss, and coming of age. Murakami's prose is captivating, and the characters are deeply relatable.", 'short_review': 'Beautifully written.', 'id': 'a289cb44-6bd8-4863-a9de-71e1921c0cda'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': 'd324d5df-fe08-4bf6-9eeb-f1cab73f121b', 'book_rating': 5, 'book_review': "1Q84 is a masterpiece of storytelling, blending elements of fantasy and mystery seamlessly. Murakami's imagination knows no bounds, and the intricate plot keeps you hooked till the end.", 'short_review': 'Masterpiece of storytelling.', 'id': '6fa8c3f9-c9e8-482b-bf3b-9d29960f2dd2'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '805bf29a-9afa-4e20-81ab-92c25868a9e2', 'book_rating': 4, 'book_review': "Harry Potter and the Chamber of Secrets is a delightful continuation of the wizarding world saga. Rowling's storytelling remains captivating, and the magical world she creates is enchanting.", 'short_review': 'Delightful continuation.', 'id': '73a95a37-0e8c-4390-9de4-35e26b56561d'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': '206b9fe4-f7c1-4549-9641-c025ce74cf06', 'book_rating': 3, 'book_review': "Norwegian Wood is a poignant tale of love and loss, but I found the pacing to be a bit slow at times. However, Murakami's introspective narrative style is still engaging.", 'short_review': 'Poignant but slow pacing.', 'id': '1ff16177-9d18-4f98-ba9c-b79b69529cc8'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': 'd324d5df-fe08-4bf6-9eeb-f1cab73f121b', 'book_rating': 5, 'book_review': "1Q84 is an enthralling journey into a surreal world where reality and fantasy intertwine. Murakami's ability to blend genres and create complex characters is unparalleled.", 'short_review': 'Enthralling journey.', 'id': 'd1e26153-3417-42b5-b21e-afffc105e703'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '805bf29a-9afa-4e20-81ab-92c25868a9e2', 'book_rating': 4, 'book_review': "Harry Potter and the Chamber of Secrets is a magical adventure that continues to captivate readers of all ages. Rowling's world-building and character development are exceptional.", 'short_review': 'Magical adventure.', 'id': '0d708dcc-7095-4f6d-b58a-7c437f73aee4'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '52767cd1-098b-46f1-9758-c8d6ceda6a69', 'book_rating': 5, 'book_review': "The Stand is an epic tale of survival and human nature. King's storytelling is masterful, and the characters are richly developed. A must-read for fans of post-apocalyptic fiction.", 'short_review': 'Masterful storytelling.', 'id': 'b50bdd44-4a74-41b9-8800-489f3099f15e'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '50617fb5-d986-4002-80f5-161bdf1bd29f', 'book_rating': 4, 'book_review': "And Still I Rise is a powerful collection of poems that inspire resilience and strength. Angelou's words resonate deeply, offering hope and empowerment to all who read them.", 'short_review': 'Powerful and inspiring.', 'id': 'e33a909c-0e4a-4551-9a57-8041532b77ff'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': 'fd2d8199-f285-4b4d-95c4-acd2b8c58023', 'book_rating': 3, 'book_review': "Cat's Cradle is an intriguing and thought-provoking novel that explores the consequences of science and technology. Vonnegut's satire is sharp, but the plot felt disjointed at times.", 'short_review': 'Intriguing but disjointed.', 'id': 'b39535c3-74b6-4a36-9490-e9a27e00455c'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '50617fb5-d986-4002-80f5-161bdf1bd29f', 'book_rating': 5, 'book_review': "And Still I Rise is a masterpiece that celebrates the resilience of the human spirit. Angelou's poetry is both empowering and uplifting, inspiring readers to overcome adversity.", 'short_review': 'Empowering masterpiece.', 'id': '690c136c-e518-42ad-8046-5717ae0d6040'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': 'ea7c29e2-a0ef-4ccd-8c13-13226fe5f9d0', 'book_rating': 3, 'book_review': "Go Set a Watchman is an intriguing sequel to To Kill a Mockingbird, offering readers a glimpse into the complexities of the characters' lives. While it lacks the impact of its predecessor, it still raises thought-provoking questions about identity and family.", 'short_review': 'Intriguing sequel.', 'id': '8f8c5572-be57-43e0-b468-35db1e872f90'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'ebce05f7-237f-410d-9d75-72b00bb1ca8b', 'book_rating': 4, 'book_review': "Fahrenheit 451 is a compelling dystopian novel that explores the dangers of censorship and the power of knowledge. Bradbury's writing is both thought-provoking and haunting, leaving a lasting impact on readers.", 'short_review': 'Compelling and thought-provoking.', 'id': 'd5f0d9b6-4745-4df4-bdb6-c73de479307e'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '94b08bcf-57a4-440f-9d04-3997e03bdb2e', 'book_rating': 2, 'book_review': 'The War of the Worlds is a classic science fiction novel that has not aged well. While the concept is interesting, the execution feels dated, and the pacing is slow. Overall, it failed to engage me as a reader.', 'short_review': 'Dated and slow-paced.', 'id': 'a98d6643-b506-4a38-972e-5171cd2dfe3a'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': 'ebce05f7-237f-410d-9d75-72b00bb1ca8b', 'book_rating': 5, 'book_review': "Fahrenheit 451 is a thought-provoking masterpiece that explores the dangers of censorship and the importance of intellectual freedom. Bradbury's prose is both poetic and powerful, making it a must-read for all lovers of literature.", 'short_review': 'Poetic masterpiece.', 'id': 'd2ce4b35-d29a-4d11-9b20-336a3d264452'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '9b22756c-bebf-4cda-a0aa-8fb22d733681', 'book_rating': 4, 'book_review': "The Tell-Tale Heart and Other Writings is a captivating collection of Edgar Allan Poe's works. Each story is masterfully crafted, drawing readers into the dark and mysterious world of Poe's imagination.", 'short_review': 'Captivating collection.', 'id': 'bd853f00-5a8f-43c2-af7d-866549674b09'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'a8d8dbe3-40ff-4784-a3db-05ad1f550185', 'book_rating': 5, 'book_review': "Selected Poems of Emily Dickinson is a beautiful anthology showcasing the poet's unique style and profound insights. Dickinson's poetry touches the soul and leaves a lasting impression on readers.", 'short_review': 'Beautiful anthology.', 'id': '27acc03f-c2b0-463a-b341-527284576007'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '4bca2528-955e-4aec-b96a-5f4afc8d8fc3', 'book_rating': 3, 'book_review': "The Weary Blues is an interesting collection of Langston Hughes' poetry, but it lacks the depth and resonance found in some of his other works. While some poems shine, others feel uninspired.", 'short_review': 'Mixed feelings.', 'id': '99389e3e-a61f-4e38-8ce5-c692f9789c5e'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': 'a8d8dbe3-40ff-4784-a3db-05ad1f550185', 'book_rating': 4, 'book_review': "Selected Poems of Emily Dickinson is a thought-provoking collection that showcases the poet's mastery of language and deep understanding of the human condition. Each poem offers a glimpse into the complexities of life and emotion.", 'short_review': 'Thought-provoking.', 'id': 'c39fb039-9701-4ab9-8964-2f2750db35d6'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': 'bf0f6e2b-2aa4-4668-a18d-5985bc3ed428', 'book_rating': 5, 'book_review': "The Collected Poems of Langston Hughes is an extraordinary compilation of his work that beautifully captures the essence of the Harlem Renaissance. Hughes' poetry resonates with timeless themes of identity, struggle, and resilience, making this collection a must-read for poetry enthusiasts.", 'short_review': 'Extraordinary.', 'id': '9a24bec5-148e-4354-b927-a42165cbadad'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '594a2650-3005-404d-85db-6a2a33040b56', 'book_rating': 4, 'book_review': "The Bell Jar offers a poignant portrayal of mental illness and societal pressures through the lens of protagonist Esther Greenwood. Sylvia Plath's prose is hauntingly beautiful, drawing readers into Esther's world of despair and introspection.", 'short_review': 'Poignant.', 'id': 'e545d2be-ed73-4536-81c7-cd96dd45b745'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'bf0f6e2b-2aa4-4668-a18d-5985bc3ed428', 'book_rating': 3, 'book_review': "While The Collected Poems of Langston Hughes showcases the poet's talent and cultural significance, some of the poems lack the depth and impact found in his more renowned works. Nonetheless, it offers valuable insights into African American history and identity.", 'short_review': 'Mixed feelings.', 'id': '7f2686a4-6e40-4560-aa33-db2dd98eb213'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '594a2650-3005-404d-85db-6a2a33040b56', 'book_rating': 2, 'book_review': "While The Bell Jar explores important themes, such as mental illness and societal expectations, Sylvia Plath's writing style can feel overly dramatic and self-indulgent at times. The protagonist's journey lacks nuance and depth, making it difficult to fully engage with the story.", 'short_review': 'Overly dramatic.', 'id': 'c178ffed-f005-4508-bee1-1e6818e52e3f'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': 'bf0f6e2b-2aa4-4668-a18d-5985bc3ed428', 'book_rating': 4, 'book_review': "The Collected Poems of Langston Hughes is a treasure trove of literary gems that celebrate the African American experience with grace and authenticity. Hughes' powerful imagery and poignant storytelling make this collection a timeless classic.", 'short_review': 'A treasure trove.', 'id': '8c0bd027-f27d-4c60-b18f-e1c644a9b766'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': '594a2650-3005-404d-85db-6a2a33040b56', 'book_rating': 3, 'book_review': "The Bell Jar provides a candid exploration of mental illness and the challenges faced by women in the 1950s. While Sylvia Plath's writing is undeniably evocative, the novel's pacing can feel sluggish, and certain passages lack clarity.", 'short_review': 'Candid exploration.', 'id': '95709e02-8c68-44d8-b6f0-62a36c817d50'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '316a8af2-1946-44ca-b01d-099130775132', 'book_rating': 4, 'book_review': "Brave New World is a thought-provoking exploration of a dystopian society where technology and conditioning control every aspect of life. While the novel's themes are compelling, some readers may find its portrayal of human nature and freedom overly pessimistic.", 'short_review': 'Thought-provoking dystopia.', 'id': 'c858f916-90f3-49de-843f-9e0dcbf4d50b'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '316a8af2-1946-44ca-b01d-099130775132', 'book_rating': 5, 'book_review': "Brave New World is a captivating critique of a society obsessed with consumerism and superficial happiness. Huxley's vision of a world where individuality is sacrificed for stability resonates deeply in today's world, making it a must-read for any lover of dystopian fiction.", 'short_review': 'Captivating critique.', 'id': '59c675e7-42fc-41b2-98e2-52cb883b2544'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '316a8af2-1946-44ca-b01d-099130775132', 'book_rating': 3, 'book_review': "While Brave New World presents a chilling vision of a future society controlled by technology and conditioning, some aspects of the novel feel dated and overly didactic. However, Huxley's exploration of themes such as individuality and conformity still holds relevance today.", 'short_review': 'Chilling vision.', 'id': '55f2a9fa-b2be-4e16-a7cd-88851ae26fc7'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': 'aea16536-842b-4108-9d5a-bb0cb5bb8704', 'book_rating': 5, 'book_review': "Moby-Dick is an epic tale that explores the depths of human obsession and the vastness of the sea. Melville's prose is rich and immersive, drawing readers into the world of whaling ships and larger-than-life characters. A must-read for anyone who loves adventure and literary depth.", 'short_review': 'Epic adventure.', 'id': 'ff8a0acb-ade2-4ac9-9895-b8ab7980f2d7'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'aea16536-842b-4108-9d5a-bb0cb5bb8704', 'book_rating': 4, 'book_review': "Moby-Dick is a towering achievement in American literature, blending adventure, philosophy, and seafaring lore into a gripping narrative. While some may find Melville's digressions and dense prose challenging, the novel's exploration of themes such as fate and revenge make it a rewarding read.", 'short_review': 'Towering achievement.', 'id': '0edf61d1-ddf2-4b50-a3ac-2dfc27c7fa1c'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'aea16536-842b-4108-9d5a-bb0cb5bb8704', 'book_rating': 3, 'book_review': "Moby-Dick is a classic work that delves into the complexities of human nature and the relentless pursuit of a goal. While Melville's prose can be dense and verbose at times, the novel's themes of obsession and fate still resonate with readers today.", 'short_review': 'Complex exploration.', 'id': 'eac33d70-17fa-4dfd-a6e3-5af50c49dfa0'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '798b9ad0-6893-4a78-aaeb-4f979fd69784', 'book_rating': 5, 'book_review': 'Little Women is a heartwarming tale of sisterhood, love, and resilience. Louisa May Alcott beautifully captures the joys and struggles of growing up, making this classic novel a timeless favorite for readers of all ages.', 'short_review': 'Heartwarming tale.', 'id': 'f302c415-8926-4fb0-80e9-5e4f31ca5edd'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '798b9ad0-6893-4a78-aaeb-4f979fd69784', 'book_rating': 4, 'book_review': "Little Women is a delightful story that celebrates the bonds of family and the pursuit of dreams. Alcott's characters are relatable and endearing, and her writing style is engaging throughout.", 'short_review': 'Delightful story.', 'id': '58fb2cf1-a63f-4d75-acf9-eb6ad079fc59'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '798b9ad0-6893-4a78-aaeb-4f979fd69784', 'book_rating': 3, 'book_review': 'While Little Women is a classic novel with memorable characters and timeless themes, some readers may find its pacing slow and its moral lessons heavy-handed. However, its exploration of sisterhood and female empowerment remains relevant today.', 'short_review': 'Memorable characters.', 'id': 'ace99d58-d660-40b4-a74e-931a8040c0bc'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'b798c783-331d-461a-b71d-e1a9ae039408', 'book_rating': 5, 'book_review': "The Picture of Dorian Gray is a gripping tale of vanity, decadence, and the consequences of unchecked ambition. Oscar Wilde's wit and satire shine through in this haunting exploration of morality and the pursuit of beauty.", 'short_review': 'Gripping tale.', 'id': '8327794d-bacc-495a-a69c-ce2dce2787e8'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'b798c783-331d-461a-b71d-e1a9ae039408', 'book_rating': 4, 'book_review': "The Picture of Dorian Gray is a mesmerizing novel that delves into the depths of human desire and the allure of eternal youth. Wilde's prose is both elegant and provocative, making this a captivating read from start to finish.", 'short_review': 'Mesmerizing novel.', 'id': '777a3f74-54cc-4ef2-9002-52cb6dabfdb4'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'b798c783-331d-461a-b71d-e1a9ae039408', 'book_rating': 3, 'book_review': "While The Picture of Dorian Gray offers a fascinating exploration of aestheticism and morality, some readers may find Wilde's philosophical digressions tedious. However, the novel's central premise and vivid imagery make it worth the read.", 'short_review': 'Fascinating exploration.', 'id': 'd8d949ab-65e8-47f5-931e-7d81f5d75325'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '69ce7a43-47fc-410a-8f95-9a16c94b1a87', 'book_rating': 5, 'book_review': "The Importance of Being Earnest is a delightful comedy filled with wit and humor. Oscar Wilde's sharp dialogue and clever wordplay make it a timeless classic that is sure to entertain readers of all ages.", 'short_review': 'Delightful comedy.', 'id': 'abe8e701-1da2-438d-9c35-b58cf68883a0'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '69ce7a43-47fc-410a-8f95-9a16c94b1a87', 'book_rating': 4, 'book_review': "The Importance of Being Earnest is a brilliant satire that offers a scathing critique of Victorian society. Wilde's clever observations and witty repartee make it a must-read for fans of classic literature.", 'short_review': 'Brilliant satire.', 'id': '9c6a5472-956e-4967-a03f-eda44b670cd9'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '69ce7a43-47fc-410a-8f95-9a16c94b1a87', 'book_rating': 3, 'book_review': 'While The Importance of Being Earnest is undeniably witty and entertaining, some readers may find its humor and social commentary dated. However, its timeless themes of love, identity, and societal expectations still resonate today.', 'short_review': 'Undeniably witty.', 'id': 'c770a6c4-8b76-4a6a-b1b3-8e7fa8053ee1'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'ca9e6acc-42f6-4d2c-991c-0741e64667c4', 'book_rating': 5, 'book_review': "The Adventures of Sherlock Holmes is a captivating collection of detective stories that showcases Arthur Conan Doyle's masterful storytelling and keen attention to detail. Each mystery is cleverly crafted, keeping readers on the edge of their seats until the very end.", 'short_review': 'Captivating collection.', 'id': '8ef6e637-efa8-4dc0-ae00-0dc114729fc4'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'ca9e6acc-42f6-4d2c-991c-0741e64667c4', 'book_rating': 4, 'book_review': "The Adventures of Sherlock Holmes is a classic work of detective fiction that has stood the test of time. Doyle's iconic character, Sherlock Holmes, is brilliantly portrayed, and each story is intricately plotted, making it a must-read for mystery enthusiasts.", 'short_review': 'Classic detective fiction.', 'id': '6f0d6bb8-ee70-4032-a6a2-747998117a79'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'ca9e6acc-42f6-4d2c-991c-0741e64667c4', 'book_rating': 3, 'book_review': 'While The Adventures of Sherlock Holmes is undeniably clever and engaging, some readers may find its formulaic structure predictable. However, the charm of Sherlock Holmes and the intrigue of the mysteries still make it a worthwhile read.', 'short_review': 'Engaging mysteries.', 'id': '25be0c86-abbc-47bb-99c9-38dc9febe8e1'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '724047b5-8329-412c-bd73-c3d6c7dc4b5d', 'book_rating': 5, 'book_review': "The Grapes of Wrath is a powerful and poignant novel that vividly captures the struggles of the Great Depression era. Steinbeck's evocative prose and compelling characters make it a hauntingly beautiful depiction of the human spirit in the face of adversity.", 'short_review': 'Powerful and poignant.', 'id': 'c58e37ea-6f8b-44f4-abcf-26f0a81bcf8e'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': '724047b5-8329-412c-bd73-c3d6c7dc4b5d', 'book_rating': 4, 'book_review': "The Grapes of Wrath is a classic American novel that offers a profound exploration of social injustice and the plight of the working class. Steinbeck's vivid descriptions and compelling narrative make it a thought-provoking read.", 'short_review': 'Profound exploration.', 'id': '483303ff-ab5d-4749-b9ba-063544386fed'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': '724047b5-8329-412c-bd73-c3d6c7dc4b5d', 'book_rating': 3, 'book_review': 'While The Grapes of Wrath is undeniably well-written and thought-provoking, some readers may find its pacing slow and its social commentary heavy-handed. However, its themes of resilience and solidarity are still relevant today.', 'short_review': 'Well-written and thought-provoking.', 'id': '444ac2e1-8d86-4fa8-8162-0fad8b2b24ae'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '99dbba88-cf20-4722-869a-887a66ac5f9a', 'book_rating': 4, 'book_review': "The Great Gatsby is a captivating novel that beautifully captures the glamour and decadence of the Jazz Age. F. Scott Fitzgerald's prose is both elegant and evocative, transporting readers to a bygone era.", 'short_review': 'Captivating novel.', 'id': '8b51b95b-895c-4d4c-bd0b-2c00688f3af6'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '99dbba88-cf20-4722-869a-887a66ac5f9a', 'book_rating': 5, 'book_review': "The Great Gatsby is a timeless classic that explores themes of love, wealth, and the American Dream. Fitzgerald's vivid characters and lyrical prose make it a must-read for literature enthusiasts.", 'short_review': 'Timeless classic.', 'id': 'a0bc6533-f89a-432b-82fd-0109f69b3b0d'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '99dbba88-cf20-4722-869a-887a66ac5f9a', 'book_rating': 3, 'book_review': 'While The Great Gatsby is undeniably well-written and atmospheric, some readers may find its characters and themes shallow. However, its depiction of the Roaring Twenties is still relevant today.', 'short_review': 'Well-written and atmospheric.', 'id': 'fdc1c811-61ff-417c-8013-03b8aba60383'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '99dbba88-cf20-4722-869a-887a66ac5f9a', 'book_rating': 2, 'book_review': 'The Great Gatsby is a disappointing read that fails to live up to its hype. While the prose is elegant, the characters are unlikable and the plot is shallow.', 'short_review': 'Disappointing read.', 'id': '09331d3e-89e0-4bff-a520-7fef80becdd5'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '90f4c594-fc80-45d3-8948-8687afe57299', 'book_rating': 5, 'book_review': "American Gods is a mesmerizing blend of mythology, fantasy, and Americana. Neil Gaiman's imagination knows no bounds, and his vivid storytelling makes this book an unforgettable journey.", 'short_review': 'Mesmerizing blend.', 'id': 'b2f7aebd-165e-45b0-a862-63e3b43c354d'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '90f4c594-fc80-45d3-8948-8687afe57299', 'book_rating': 4, 'book_review': "American Gods is a unique and captivating novel that explores the nature of belief and the power of myth. Gaiman's prose is both lyrical and thought-provoking, making it a must-read for fans of fantasy.", 'short_review': 'Unique and captivating.', 'id': '749d63c0-51b7-444c-a0e8-eef30f17617b'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '90f4c594-fc80-45d3-8948-8687afe57299', 'book_rating': 3, 'book_review': 'While American Gods is undeniably ambitious and imaginative, some readers may find its pacing slow and its plot convoluted. However, its rich mythology and complex characters make it a rewarding read for those who persevere.', 'short_review': 'Ambitious and imaginative.', 'id': '890fbf8e-3ed9-4fed-896a-9308dfc231b1'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '7c5443be-10b1-4f70-a30f-58382b6971b0', 'book_rating': 4, 'book_review': "Do Androids Dream of Electric Sheep? is a thought-provoking science fiction novel that raises important questions about identity, empathy, and the nature of humanity. Philip K. Dick's vision of a dystopian future is both chilling and compelling.", 'short_review': 'Thought-provoking science fiction.', 'id': '3ec04f42-d878-4d48-8ebf-8e659604f811'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': '7c5443be-10b1-4f70-a30f-58382b6971b0', 'book_rating': 3, 'book_review': "Do Androids Dream of Electric Sheep? is a fascinating exploration of artificial intelligence and what it means to be human. While the pacing can be slow at times, Dick's philosophical insights make it a worthwhile read.", 'short_review': 'Fascinating exploration.', 'id': 'ec22ac08-5a50-4e1e-8d52-575ccb72826f'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': '7c5443be-10b1-4f70-a30f-58382b6971b0', 'book_rating': 5, 'book_review': "Do Androids Dream of Electric Sheep? is a masterpiece of science fiction that remains relevant in today's world of advancing technology. Dick's exploration of the blurred lines between man and machine is both thought-provoking and deeply moving.", 'short_review': 'Masterpiece of science fiction.', 'id': '6d7b8f5f-a7c7-4d04-8880-8e8ee2958649'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': 'a2d912c2-257e-4028-a0ec-9bda804742e5', 'book_rating': 4, 'book_review': "The Man in the High Castle is a thought-provoking alternative history novel that explores the consequences of a world where the Axis powers won World War II. Philip K. Dick's imaginative storytelling and attention to detail make it a compelling read.", 'short_review': 'Thought-provoking alternative history.', 'id': 'fe8b8e5b-6f2d-4f27-9960-33c6a2bc7e42'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': 'a2d912c2-257e-4028-a0ec-9bda804742e5', 'book_rating': 5, 'book_review': "The Man in the High Castle is a masterpiece of speculative fiction that offers a chilling glimpse into a world where the Nazis and Japanese have divided America. Dick's exploration of identity and reality is both profound and unsettling.", 'short_review': 'Masterpiece of speculative fiction.', 'id': '571c23ba-456d-4837-86d9-019eff8518cb'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': 'a2d912c2-257e-4028-a0ec-9bda804742e5', 'book_rating': 3, 'book_review': 'While The Man in the High Castle presents an intriguing premise, some readers may find its pacing uneven and its plot convoluted. However, its exploration of alternate history and moral ambiguity still makes it a worthwhile read.', 'short_review': 'Intriguing premise.', 'id': '86f83dfc-7b77-477e-be95-11b63257cb4d'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': 'a2d912c2-257e-4028-a0ec-9bda804742e5', 'book_rating': 2, 'book_review': 'The Man in the High Castle is a disappointing novel that fails to deliver on its intriguing premise. The narrative lacks coherence, and the characters feel underdeveloped.', 'short_review': 'Disappointing read.', 'id': '8ffaee7b-76bd-4986-bbab-66614952f230'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'eb9a566a-7020-4ef8-b168-3d68aa39d23c', 'book_rating': 5, 'book_review': "The Handmaid's Tale is a chilling dystopian novel that offers a stark warning about the dangers of totalitarianism and the erosion of women's rights. Margaret Atwood's prose is both lyrical and haunting, making it a powerful and unforgettable read.", 'short_review': 'Chilling dystopian novel.', 'id': '5ca7e050-7296-4bbb-b90b-e4ded2d73e67'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'eb9a566a-7020-4ef8-b168-3d68aa39d23c', 'book_rating': 4, 'book_review': "The Handmaid's Tale is a provocative and timely novel that explores issues of power, control, and gender oppression. Atwood's stark portrayal of a dystopian society is both unsettling and thought-provoking.", 'short_review': 'Provocative and timely.', 'id': 'bfef4674-5faf-4c51-b962-d82a2455cf7c'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'eb9a566a-7020-4ef8-b168-3d68aa39d23c', 'book_rating': 3, 'book_review': "While The Handmaid's Tale is undeniably well-written and thought-provoking, some readers may find its pacing slow and its narrative structure disjointed. However, its themes of oppression and resistance are still relevant today.", 'short_review': 'Well-written but slow pacing.', 'id': 'eab35310-41f0-48f7-b894-160e1b8d7bae'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': 'cb537a82-c01f-47ec-b4f4-6437c2134f93', 'book_rating': 4, 'book_review': "Oryx and Crake is a compelling and thought-provoking dystopian novel that explores the consequences of genetic engineering and corporate greed. Margaret Atwood's vivid imagination and dark humor make it a must-read for fans of speculative fiction.", 'short_review': 'Compelling and thought-provoking.', 'id': 'efd85126-c42a-4920-826f-d3ae21a3cf12'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': 'cb537a82-c01f-47ec-b4f4-6437c2134f93', 'book_rating': 3, 'book_review': "Oryx and Crake presents an intriguing vision of a future ravaged by scientific experimentation and environmental collapse. Atwood's prose is vivid, but the novel's bleak outlook may be too dark for some readers.", 'short_review': 'Intriguing vision.', 'id': '099a412b-5c05-4ac8-be0b-b962597f4618'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': 'cb537a82-c01f-47ec-b4f4-6437c2134f93', 'book_rating': 5, 'book_review': "Oryx and Crake is a haunting and unforgettable exploration of humanity's destructive tendencies and the consequences of unchecked scientific progress. Atwood's writing is both beautiful and chilling, making it a standout in the dystopian genre.", 'short_review': 'Haunting and unforgettable.', 'id': '5cdbb40e-16c7-40aa-9f73-fc511e0aa4ed'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '5240bed8-6928-4cec-954e-9461038dc774', 'book_rating': 4, 'book_review': "My Name Is Red is a captivating novel that immerses readers in the vibrant world of Ottoman Istanbul. Orhan Pamuk's intricate storytelling and rich descriptions make it a truly memorable read.", 'short_review': 'Captivating historical novel.', 'id': 'e82af615-f5d8-479d-810c-d93ab62ffbbd'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '5240bed8-6928-4cec-954e-9461038dc774', 'book_rating': 5, 'book_review': "My Name Is Red is a masterpiece of storytelling that skillfully blends history, mystery, and art. Pamuk's prose is elegant and evocative, transporting readers to a bygone era.", 'short_review': 'Masterpiece of storytelling.', 'id': '7d3e151d-03ce-4e99-8b64-35ce411b6cbb'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '5240bed8-6928-4cec-954e-9461038dc774', 'book_rating': 3, 'book_review': 'While My Name Is Red offers a fascinating glimpse into Ottoman culture and art, some readers may find its pacing slow and its plot overly complex. However, its exploration of love and betrayal still makes it worth reading.', 'short_review': 'Fascinating but slow-paced.', 'id': '716d0dab-a71a-4f9f-96a7-f298c85343db'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '5240bed8-6928-4cec-954e-9461038dc774', 'book_rating': 2, 'book_review': 'My Name Is Red is a disappointing novel that fails to live up to its intriguing premise. The narrative is disjointed, and the characters lack depth, making it a struggle to stay engaged.', 'short_review': 'Disappointing read.', 'id': '14fca63b-ee1f-45b7-a988-b05fc897b63e'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'ef0dd284-1dec-470c-86e4-efa6673688f8', 'book_rating': 5, 'book_review': "The House of the Spirits is a mesmerizing family saga that spans generations and blends magical realism with political upheaval. Isabel Allende's lush prose and vivid characters make it a literary masterpiece.", 'short_review': 'Mesmerizing family saga.', 'id': '6eba7a76-7a56-4318-8ea1-9475e43e86c4'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'ef0dd284-1dec-470c-86e4-efa6673688f8', 'book_rating': 4, 'book_review': "The House of the Spirits is an enchanting novel that explores themes of love, power, and destiny against the backdrop of political turmoil. Allende's lyrical prose and vivid imagery create a world that lingers in the imagination.", 'short_review': 'Enchanting exploration of love and destiny.', 'id': '2a043540-2d2d-4bcf-8bfe-896bb784cfae'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'ef0dd284-1dec-470c-86e4-efa6673688f8', 'book_rating': 3, 'book_review': 'While The House of the Spirits boasts lush prose and an ambitious narrative, some readers may find its length daunting and its plot meandering. However, its exploration of familial bonds and societal change is still compelling.', 'short_review': 'Lush prose but meandering plot.', 'id': '570e1b15-c22d-4d00-9058-6d5a623ab4c0'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': 'b8a5caad-d6d7-4f3d-9522-bfcfe0a5f049', 'book_rating': 4, 'book_review': "Never Let Me Go is a haunting and thought-provoking novel that explores the ethics of cloning and the nature of humanity. Kazuo Ishiguro's subtle storytelling and nuanced characters leave a lasting impact on readers.", 'short_review': 'Haunting exploration of ethics.', 'id': '4638615d-ee4a-45fb-8647-82a228c52f66'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': 'b8a5caad-d6d7-4f3d-9522-bfcfe0a5f049', 'book_rating': 3, 'book_review': 'Never Let Me Go presents a compelling premise and raises important ethical questions, but some readers may find its melancholic tone overwhelming. However, its exploration of love and loss is undeniably moving.', 'short_review': 'Compelling premise but melancholic tone.', 'id': 'c88ff0b9-802b-4ea2-a87e-79440a524111'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': 'b8a5caad-d6d7-4f3d-9522-bfcfe0a5f049', 'book_rating': 5, 'book_review': "Never Let Me Go is a beautiful and haunting novel that delves into the human condition and the fragility of life. Ishiguro's prose is luminous, and his exploration of memory and identity is deeply affecting.", 'short_review': 'Beautiful and haunting.', 'id': '984208d6-dd3b-417c-b582-0668bed702ca'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '495f4da7-6dda-47c9-b012-8df9fc7538c7', 'book_rating': 4, 'book_review': "The Golden Notebook is a powerful and thought-provoking novel that delves into the complexities of identity and relationships. Doris Lessing's writing is both intimate and insightful, making it a compelling read.", 'short_review': 'Powerful and thought-provoking.', 'id': '04c43198-f71c-48c7-9f30-e83afd55d0ab'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '495f4da7-6dda-47c9-b012-8df9fc7538c7', 'book_rating': 5, 'book_review': "The Golden Notebook is a literary masterpiece that boldly explores themes of feminism, politics, and mental health. Lessing's narrative structure is innovative, and her characters are deeply human and relatable.", 'short_review': 'Literary masterpiece.', 'id': '046cace1-b811-4d88-a9dc-7868c5a8a2be'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '495f4da7-6dda-47c9-b012-8df9fc7538c7', 'book_rating': 3, 'book_review': 'While The Golden Notebook offers a unique perspective on gender and society, some readers may find its nonlinear narrative confusing. However, its exploration of female identity is still relevant and compelling.', 'short_review': 'Unique perspective but confusing.', 'id': '287a7568-3ac7-476a-8256-38e004105f6f'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '495f4da7-6dda-47c9-b012-8df9fc7538c7', 'book_rating': 2, 'book_review': "The Golden Notebook is a disappointing read with flat characters and a disjointed plot. Lessing's attempt to tackle multiple themes results in a messy narrative that fails to engage.", 'short_review': 'Disappointing and messy.', 'id': '82a12537-db4c-4c16-ad6b-152466662a2b'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '9c9b218a-a058-487c-8377-f95871c61f44', 'book_rating': 5, 'book_review': "Lolita is a beautifully written but disturbing novel that challenges readers with its provocative subject matter. Vladimir Nabokov's prose is exquisite, and his exploration of obsession and morality is masterful.", 'short_review': 'Beautiful but disturbing.', 'id': 'b0b42ca4-2c15-471c-afcf-43e94d00e94b'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '9c9b218a-a058-487c-8377-f95871c61f44', 'book_rating': 4, 'book_review': "Lolita is a controversial yet captivating novel that showcases Nabokov's unparalleled literary talent. The story's unreliable narrator adds depth to its exploration of taboo subjects, making it a compelling read.", 'short_review': 'Controversial yet captivating.', 'id': '4ec1f51e-b890-4725-9c68-2dd90f7295ad'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '9c9b218a-a058-487c-8377-f95871c61f44', 'book_rating': 3, 'book_review': "While Lolita is undeniably well-written, some readers may find its subject matter deeply unsettling. Nabokov's lyrical prose cannot fully overshadow the discomfort caused by the novel's themes.", 'short_review': 'Well-written but unsettling.', 'id': '5df0c8b2-9763-45df-a9e1-cb68c951f5fd'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': 'c1eeea5b-12a6-4044-a2db-88171076226a', 'book_rating': 4, 'book_review': "Midnight's Children is a sprawling and ambitious novel that masterfully blends history with magical realism. Salman Rushdie's vivid imagery and lyrical prose create a vivid tapestry of postcolonial India.", 'short_review': 'Sprawling and ambitious.', 'id': '10e005ac-2a9c-46ea-a4ff-50c326b75b9f'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': 'c1eeea5b-12a6-4044-a2db-88171076226a', 'book_rating': 3, 'book_review': "Midnight's Children is an impressive literary feat, but its dense prose and convoluted narrative may be challenging for some readers to navigate. Rushdie's exploration of India's history is nonetheless compelling.", 'short_review': 'Impressive but challenging.', 'id': '1f772355-ebcd-4a3f-b5b5-5f50d4f25f65'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': 'c1eeea5b-12a6-4044-a2db-88171076226a', 'book_rating': 5, 'book_review': "Midnight's Children is a masterpiece that captures the tumultuous history of India with grace and imagination. Rushdie's narrative prowess and rich symbolism make it a must-read for fans of postcolonial literature.", 'short_review': 'Masterpiece of postcolonial literature.', 'id': '5be4e0e0-6735-4f06-a8bf-d45a0d8fcd5f'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': 'c2188b1f-b9be-492f-9b9c-556ab44342b5', 'book_rating': 4, 'book_review': "The Road is a haunting and powerful post-apocalyptic novel that explores the depths of human resilience and the bond between father and son. Cormac McCarthy's spare prose style adds to the atmosphere of despair and hope.", 'short_review': 'Haunting and powerful.', 'id': '2189add3-f419-4883-8160-21c0bae14989'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': 'c2188b1f-b9be-492f-9b9c-556ab44342b5', 'book_rating': 5, 'book_review': "The Road is a masterpiece that evokes a sense of existential dread while also celebrating the human spirit. McCarthy's prose is poetic and visceral, painting a vivid portrait of a desolate world.", 'short_review': 'Masterpiece of existential dread.', 'id': '255ddd47-7336-4cca-af9e-7e29e07304dd'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': 'c2188b1f-b9be-492f-9b9c-556ab44342b5', 'book_rating': 3, 'book_review': "While The Road offers a bleak and thought-provoking glimpse into a post-apocalyptic future, some readers may find its narrative too bleak and its themes too heavy-handed. However, McCarthy's prose is undeniably powerful.", 'short_review': 'Bleak but thought-provoking.', 'id': '26d16807-d1be-4dcc-8bd8-d5037859499a'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': 'c2188b1f-b9be-492f-9b9c-556ab44342b5', 'book_rating': 2, 'book_review': "The Road is a tedious and overrated novel that fails to deliver on its promise of profundity. McCarthy's sparse prose style becomes monotonous, and the story lacks depth and character development.", 'short_review': 'Tedious and overrated.', 'id': '7a258856-29aa-42b9-97be-53ab76219fa6'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '8811f52e-6e18-424d-95d9-954cebd53302', 'book_rating': 5, 'book_review': "The Catcher in the Rye is a timeless coming-of-age novel that resonates with readers of all ages. J.D. Salinger's portrayal of teenage angst and alienation is both poignant and relatable, making it a classic.", 'short_review': 'Timeless coming-of-age classic.', 'id': 'ccbd8c12-0b7c-48d8-aa67-50c3f17e92c4'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '8811f52e-6e18-424d-95d9-954cebd53302', 'book_rating': 4, 'book_review': "The Catcher in the Rye captures the disillusionment and rebellion of youth with honesty and authenticity. Holden Caulfield's voice is distinct and unforgettable, making this novel a must-read for teenagers and adults alike.", 'short_review': 'Unforgettable voice of youth.', 'id': 'b988a484-4ccc-46e8-aa3c-41414c2145e5'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '8811f52e-6e18-424d-95d9-954cebd53302', 'book_rating': 3, 'book_review': "While The Catcher in the Rye offers an insightful portrayal of adolescent angst, some readers may find Holden Caulfield's cynicism grating. Salinger's narrative style can be repetitive, but the novel still has its moments.", 'short_review': 'Insightful but repetitive.', 'id': 'dd77962b-631c-4770-b3f7-53d385fea465'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': 'bc5b3eba-b5a3-4f30-b133-37791b5b0ef4', 'book_rating': 4, 'book_review': "The Color Purple is a powerful and deeply moving novel that explores themes of race, gender, and identity. Alice Walker's prose is lyrical and evocative, and her characters are unforgettable.", 'short_review': 'Powerful and deeply moving.', 'id': '94a0a977-2264-4963-890d-e4d5d3795c10'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': 'bc5b3eba-b5a3-4f30-b133-37791b5b0ef4', 'book_rating': 3, 'book_review': "While The Color Purple tackles important issues with sensitivity and insight, some readers may find its narrative structure confusing. Nonetheless, Alice Walker's storytelling is powerful and emotionally resonant.", 'short_review': 'Sensitive but confusing.', 'id': '2e669aad-feea-40b0-b620-57649be3d5b9'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': 'bc5b3eba-b5a3-4f30-b133-37791b5b0ef4', 'book_rating': 5, 'book_review': "The Color Purple is a triumph of literature, tackling difficult themes with grace and humanity. Walker's characters are richly drawn, and her prose is both lyrical and powerful. A must-read for anyone interested in social justice.", 'short_review': 'Triumph of literature.', 'id': '31c4411c-d53d-476a-94ae-3de49ba1bf00'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '4de2c275-4077-49d9-9f68-c92621294160', 'book_rating': 4, 'book_review': "Things Fall Apart is a poignant portrayal of the clash between traditional African culture and colonialism. Chinua Achebe's vivid descriptions and compelling characters make this a must-read for anyone interested in African literature.", 'short_review': 'Poignant portrayal.', 'id': 'db22871f-df2e-44cb-b72c-7451cd2e6e7e'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '4de2c275-4077-49d9-9f68-c92621294160', 'book_rating': 5, 'book_review': "Things Fall Apart is a powerful novel that delves into the complexities of Nigerian society before and after colonization. Achebe's storytelling is masterful, and the themes of identity and cultural change resonate deeply.", 'short_review': 'Powerful storytelling.', 'id': '386f1e49-e8b8-4e0b-9856-ad28b864009d'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '4de2c275-4077-49d9-9f68-c92621294160', 'book_rating': 3, 'book_review': "While Things Fall Apart offers valuable insights into Nigerian culture and history, some readers may find the pacing slow and the prose dense. However, Achebe's exploration of colonialism and its impact remains relevant.", 'short_review': 'Valuable insights.', 'id': '3edebdc9-1564-4cc2-9673-f335cda639df'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '4de2c275-4077-49d9-9f68-c92621294160', 'book_rating': 2, 'book_review': 'Things Fall Apart failed to engage me as a reader. The narrative felt disjointed, and the characters lacked depth. While the themes are important, I found the execution lacking.', 'short_review': 'Failed to engage.', 'id': 'c2a1db50-66a3-4d87-8e92-1ba760be3496'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'e776150b-cd36-4c0f-8178-079bbd3c6622', 'book_rating': 5, 'book_review': "The Diary of a Young Girl is a harrowing account of Anne Frank's experiences during the Holocaust. Her courage and resilience in the face of unimaginable adversity are inspiring. Every page is imbued with hope and humanity.", 'short_review': 'Harrowing and inspiring.', 'id': 'ca340070-5bc4-4593-9f37-b272ef3e5baa'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'e776150b-cd36-4c0f-8178-079bbd3c6622', 'book_rating': 4, 'book_review': "The Diary of a Young Girl offers a unique perspective on the Holocaust through the eyes of a young girl. Anne Frank's diary is both heartbreaking and hopeful, reminding us of the power of resilience and the human spirit.", 'short_review': 'Heartbreaking and hopeful.', 'id': 'a5c0bb60-be03-49ea-a1ed-d2cfb31fce30'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'e776150b-cd36-4c0f-8178-079bbd3c6622', 'book_rating': 3, 'book_review': "While The Diary of a Young Girl provides valuable insights into the Holocaust, some readers may find Anne Frank's writing style repetitive. Nonetheless, her story remains a poignant reminder of the horrors of war.", 'short_review': 'Valuable insights.', 'id': '52aecff2-6262-46f7-b72b-32e1660832d8'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '82411803-f697-4503-bce7-7636bd3a6acc', 'book_rating': 4, 'book_review': "Jane Eyre is a timeless classic that explores themes of love, independence, and social class. Charlotte Bront�'s vivid characters and rich prose make this a captivating read for lovers of Victorian literature.", 'short_review': 'Timeless classic.', 'id': 'eabe0430-12cc-474b-950f-8c2a8614e2af'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': '82411803-f697-4503-bce7-7636bd3a6acc', 'book_rating': 3, 'book_review': "While Jane Eyre is a well-written novel with complex characters, some readers may find the pacing slow, especially in the early chapters. However, Bront�'s exploration of social issues is still relevant today.", 'short_review': 'Well-written but slow pacing.', 'id': 'b149ed7b-53d3-4492-8b81-ae2e2d7b5750'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': '82411803-f697-4503-bce7-7636bd3a6acc', 'book_rating': 5, 'book_review': "Jane Eyre is a masterpiece of English literature, blending romance, mystery, and social commentary seamlessly. Bront�'s portrayal of Jane's inner strength and resilience continues to captivate readers of all ages.", 'short_review': 'Masterpiece of English literature.', 'id': '70d26c56-1e25-46d7-8595-415989978104'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '93cf0e9c-5936-4a98-8500-0840bb7b7740', 'book_rating': 4, 'book_review': "Frankenstein is a gripping tale of science, ambition, and morality. Mary Shelley's exploration of the consequences of playing god is as relevant today as it was when the novel was first published.", 'short_review': 'Gripping tale.', 'id': 'b4e1445e-5de5-403e-89be-c3c0cb948765'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '93cf0e9c-5936-4a98-8500-0840bb7b7740', 'book_rating': 5, 'book_review': "Frankenstein is a masterpiece of Gothic literature that delves into themes of ambition, isolation, and the nature of humanity. Mary Shelley's prose is both haunting and beautiful, making this a timeless classic.", 'short_review': 'Timeless classic.', 'id': 'e2a7bed9-12ff-43e9-bd04-ace654c2826e'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '93cf0e9c-5936-4a98-8500-0840bb7b7740', 'book_rating': 3, 'book_review': "While Frankenstein is undeniably a classic, some readers may find the pacing slow, especially in the middle sections. However, the novel's exploration of scientific ethics remains thought-provoking.", 'short_review': 'Classic but slow pacing.', 'id': 'f8d09c17-13f5-45d9-8f3a-6cd586682b53'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '93cf0e9c-5936-4a98-8500-0840bb7b7740', 'book_rating': 2, 'book_review': 'Frankenstein failed to captivate me as a reader. The narrative felt disjointed, and the characters lacked depth. While the premise is intriguing, the execution fell short of my expectations.', 'short_review': 'Failed to captivate.', 'id': 'd59d576c-a66b-44a9-a483-aba644376a18'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'dd6a3890-d32a-40ee-ba83-4eab184ee48a', 'book_rating': 5, 'book_review': "The Count of Monte Cristo is an epic tale of revenge, betrayal, and redemption. Alexandre Dumas's intricate plot and vivid characters kept me on the edge of my seat from beginning to end. A true masterpiece.", 'short_review': 'Epic tale.', 'id': '34695b49-f9e4-4c3e-9b89-a0423fdb28b6'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'dd6a3890-d32a-40ee-ba83-4eab184ee48a', 'book_rating': 4, 'book_review': "The Count of Monte Cristo is a riveting adventure that explores themes of justice and forgiveness. While the story is lengthy, every twist and turn is worth the journey. Dumas's storytelling prowess shines in this classic.", 'short_review': 'Riveting adventure.', 'id': '3aabb50f-09eb-4909-8eb1-70fd6fd96e56'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'dd6a3890-d32a-40ee-ba83-4eab184ee48a', 'book_rating': 3, 'book_review': "While The Count of Monte Cristo is an engaging tale, some readers may find the plot convoluted and the pacing uneven. However, the novel's exploration of revenge and forgiveness is thought-provoking.", 'short_review': 'Engaging but convoluted.', 'id': '8de784ec-8a89-4372-a143-17baa310ce18'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': 'fdce9426-a4f5-4eca-bc9e-6577c007017d', 'book_rating': 4, 'book_review': "A Tale of Two Cities is a compelling historical novel set against the backdrop of the French Revolution. Charles Dickens's vivid descriptions and memorable characters make this a must-read for fans of classic literature.", 'short_review': 'Compelling historical novel.', 'id': '39ce6cd8-fee4-443d-ab51-6546ef927a46'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': 'fdce9426-a4f5-4eca-bc9e-6577c007017d', 'book_rating': 3, 'book_review': "While A Tale of Two Cities offers a fascinating glimpse into the French Revolution, some readers may find Dickens's writing style verbose and the plot overly melodramatic. Nonetheless, the novel's themes of sacrifice and redemption are timeless.", 'short_review': 'Fascinating but verbose.', 'id': '80ca38d0-707c-4f17-8d7b-fe75ed00cc70'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': 'fdce9426-a4f5-4eca-bc9e-6577c007017d', 'book_rating': 5, 'book_review': "A Tale of Two Cities is a literary masterpiece that captures the tumultuous spirit of the French Revolution. Dickens's rich storytelling and poignant themes of sacrifice and resurrection make this a timeless classic.", 'short_review': 'Literary masterpiece.', 'id': '5046c79a-f0be-4003-b504-7676964446a2'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '2afe9fc2-d209-46a4-a4fb-f77d808368e4', 'book_rating': 4, 'book_review': "The Jungle Book is a classic collection of stories that vividly brings the jungle to life. Rudyard Kipling's imaginative tales captivate readers of all ages with their adventure and charm.", 'short_review': 'Captivating tales.', 'id': 'f0ba6e92-dac1-437c-891a-24ab1e223113'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '2afe9fc2-d209-46a4-a4fb-f77d808368e4', 'book_rating': 5, 'book_review': "The Jungle Book is a timeless masterpiece that transports readers into the heart of the jungle. Kipling's rich descriptions and memorable characters make this a must-read for anyone who loves adventure.", 'short_review': 'Timeless masterpiece.', 'id': '7a755ff6-7965-44ff-ba4b-65f0c4b81495'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '2afe9fc2-d209-46a4-a4fb-f77d808368e4', 'book_rating': 3, 'book_review': "While The Jungle Book is a classic work of literature, some readers may find the language and themes outdated. However, Kipling's storytelling still holds a certain charm that can appeal to those interested in adventure.", 'short_review': 'Outdated themes.', 'id': '808f5252-0c31-4145-b39e-01ba5e2d676e'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '2afe9fc2-d209-46a4-a4fb-f77d808368e4', 'book_rating': 2, 'book_review': 'The Jungle Book failed to capture my interest. The stories felt disjointed, and the characters lacked depth. While it may have been groundbreaking in its time, it does not resonate with modern readers.', 'short_review': 'Lacked depth.', 'id': '81e744f9-a6dc-4cb1-839c-0556bbfc4635'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '80c39dff-06b6-489d-8169-bb58b0ba1f8c', 'book_rating': 5, 'book_review': "Madame Bovary is a powerful exploration of desire, betrayal, and societal expectations. Gustave Flaubert's prose is exquisite, painting a vivid portrait of Emma Bovary's tragic life.", 'short_review': 'Powerful exploration.', 'id': '0fb1b85f-37b0-4a5c-84a1-ec02e4d55f72'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '80c39dff-06b6-489d-8169-bb58b0ba1f8c', 'book_rating': 4, 'book_review': "Madame Bovary offers a compelling glimpse into the complexities of human nature. Flaubert's attention to detail and character development make this a timeless classic that continues to resonate with readers.", 'short_review': 'Compelling glimpse.', 'id': 'd08dd729-0d71-40f6-bbf0-d74fbfaf88ca'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '80c39dff-06b6-489d-8169-bb58b0ba1f8c', 'book_rating': 3, 'book_review': "While Madame Bovary is undeniably well-written, I found the protagonist's actions frustrating and the plot slow-paced. However, Flaubert's exploration of societal norms and gender roles is thought-provoking.", 'short_review': 'Frustrating protagonist.', 'id': '98a62992-7404-4ad6-8a52-63e26704a905'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '2ddb6885-f7de-4302-a0a7-e949d39f3204', 'book_rating': 4, 'book_review': "The Scarlet Letter is a classic novel that delves into themes of sin, guilt, and redemption. Nathaniel Hawthorne's prose is elegant and evocative, making this a compelling read from start to finish.", 'short_review': 'Compelling read.', 'id': '08a397d2-fb08-4202-b12d-1b9196cde63b'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': '2ddb6885-f7de-4302-a0a7-e949d39f3204', 'book_rating': 3, 'book_review': "The Scarlet Letter is a thought-provoking novel that explores the consequences of societal judgment and hypocrisy. While Hawthorne's writing style may be dense for some, the themes remain relevant to contemporary society.", 'short_review': 'Thought-provoking.', 'id': '1baec5f6-5c4d-4dd0-b9eb-fb64a8e407ab'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': '2ddb6885-f7de-4302-a0a7-e949d39f3204', 'book_rating': 5, 'book_review': "The Scarlet Letter is a timeless masterpiece that continues to resonate with readers today. Hawthorne's exploration of sin and redemption is profound, and the novel's themes are as relevant now as they were in the 19th century.", 'short_review': 'Timeless masterpiece.', 'id': '04ed4168-9c0b-4305-9e0e-a30fa42a20dd'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '5fc4c664-a78e-45d8-964a-530ce1c97049', 'book_rating': 4, 'book_review': "Middlemarch is a rich and complex novel that delves deep into the lives of its characters. George Eliot's insightful commentary on society and human nature makes this a rewarding read.", 'short_review': 'Rich and complex.', 'id': '1df54307-7d27-40cf-a330-ac3c82e50b70'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '5fc4c664-a78e-45d8-964a-530ce1c97049', 'book_rating': 5, 'book_review': "Middlemarch is a masterpiece of Victorian literature. Eliot's vivid portrayal of provincial life and her nuanced characters make this novel a timeless classic.", 'short_review': 'Timeless classic.', 'id': 'bd49ebc8-0a3c-44c7-a197-e24fe9840904'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '5fc4c664-a78e-45d8-964a-530ce1c97049', 'book_rating': 3, 'book_review': 'While Middlemarch is undoubtedly a well-crafted novel, its length and dense prose may deter some readers. However, those who persevere will find a rewarding exploration of human relationships.', 'short_review': 'Dense prose.', 'id': 'a75a1197-dced-4998-a1fd-191b92bf9789'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '5fc4c664-a78e-45d8-964a-530ce1c97049', 'book_rating': 2, 'book_review': 'Middlemarch was a disappointing read for me. The slow pace and multitude of characters made it difficult to engage with the story. While some may appreciate its depth, I found it tedious.', 'short_review': 'Disappointing read.', 'id': '3ba4e68b-250e-4f18-9ba2-022d057652cc'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'ed7998de-e7d2-4c18-a659-174820e7d9b1', 'book_rating': 5, 'book_review': "A Doll's House is a groundbreaking play that challenges societal norms and expectations. Henrik Ibsen's exploration of gender roles and identity is as relevant today as it was when the play was first performed.", 'short_review': 'Groundbreaking play.', 'id': '2aa885f0-51c2-4888-9b48-d9e6a57c69ab'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'ed7998de-e7d2-4c18-a659-174820e7d9b1', 'book_rating': 4, 'book_review': "A Doll's House is a thought-provoking play that raises important questions about marriage and individual freedom. Ibsen's skillful storytelling and memorable characters make this a must-read for anyone interested in social issues.", 'short_review': 'Thought-provoking.', 'id': '1ddb4f08-cffc-46ee-bb6c-6fde918cfaa8'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'ed7998de-e7d2-4c18-a659-174820e7d9b1', 'book_rating': 3, 'book_review': "While A Doll's House addresses significant themes, I found the characters and dialogue somewhat melodramatic. However, I appreciate its historical importance and impact on feminist literature.", 'short_review': 'Melodramatic.', 'id': '20cf6ea4-ea67-45f0-832f-2ca3392e69f8'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': 'b113c266-e5d3-47fd-92ab-6112915d21f8', 'book_rating': 4, 'book_review': "Tess of the d'Urbervilles is a tragic yet compelling tale of innocence lost and societal injustice. Thomas Hardy's poetic prose and vivid descriptions bring the English countryside to life.", 'short_review': 'Tragic yet compelling.', 'id': 'f75289f6-3842-412c-b46e-08e4e1b1cdf6'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': 'b113c266-e5d3-47fd-92ab-6112915d21f8', 'book_rating': 3, 'book_review': "Tess of the d'Urbervilles is a somber novel that highlights the harsh realities faced by women in Victorian England. While Hardy's writing is beautiful, the bleakness of the story may be off-putting for some.", 'short_review': 'Somber novel.', 'id': '926fc70d-cdf0-4252-834b-ede18abccaf2'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': 'b113c266-e5d3-47fd-92ab-6112915d21f8', 'book_rating': 5, 'book_review': "Tess of the d'Urbervilles is a masterpiece of English literature. Hardy's exploration of themes such as fate, morality, and the plight of women is both profound and moving. A must-read for lovers of classic literature.", 'short_review': 'Masterpiece.', 'id': '3edea765-469e-4173-b406-5c0787789b8c'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '2888a4bb-9c18-4bf5-b512-61e9c4fd659f', 'book_rating': 4, 'book_review': "The Turn of the Screw is a chilling tale that keeps you on the edge of your seat. Henry James's mastery of suspense and psychological horror makes this a classic ghost story.", 'short_review': 'Chilling tale.', 'id': 'a77b6709-a7ec-4ea9-96b3-92fdb8bf1ccb'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '2888a4bb-9c18-4bf5-b512-61e9c4fd659f', 'book_rating': 5, 'book_review': "The Turn of the Screw is a masterpiece of ambiguity and suspense. Henry James's exploration of the supernatural and the psychological is both gripping and thought-provoking.", 'short_review': 'Masterpiece of ambiguity.', 'id': '59ec2f20-ef9a-4410-b983-2c958d518259'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '2888a4bb-9c18-4bf5-b512-61e9c4fd659f', 'book_rating': 3, 'book_review': 'While The Turn of the Screw has its moments of suspense, I found the ambiguity frustrating. The lack of clarity regarding the supernatural elements detracted from my enjoyment of the story.', 'short_review': 'Frustrating ambiguity.', 'id': '31f89f51-3477-433c-bab9-ab853cd1c4e0'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '2888a4bb-9c18-4bf5-b512-61e9c4fd659f', 'book_rating': 2, 'book_review': 'The Turn of the Screw left me feeling underwhelmed. The pacing was slow, and the plot felt disjointed. While I appreciate its literary significance, I struggled to connect with the story.', 'short_review': 'Underwhelming.', 'id': '36e6df27-da4b-46c6-854f-13226aa2faaa'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'dcd8068f-afad-476e-9496-be37f63b341d', 'book_rating': 5, 'book_review': "The Awakening is a powerful and poignant novel that explores themes of female independence and self-discovery. Kate Chopin's lyrical prose and insightful portrayal of Edna Pontellier's journey make this a timeless classic.", 'short_review': 'Powerful and poignant.', 'id': '6fe54472-3570-46ec-949a-9dcc3d1730e1'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'dcd8068f-afad-476e-9496-be37f63b341d', 'book_rating': 4, 'book_review': "The Awakening is a thought-provoking novel that challenges societal norms and expectations. Kate Chopin's exploration of female identity and desire is as relevant today as it was when the book was first published.", 'short_review': 'Thought-provoking.', 'id': 'bce393a0-5fd6-4303-8705-4f204eb18792'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'dcd8068f-afad-476e-9496-be37f63b341d', 'book_rating': 3, 'book_review': "While The Awakening addresses important themes, I found the protagonist's actions to be frustrating at times. However, Chopin's exploration of women's roles in society is still relevant today.", 'short_review': 'Frustrating protagonist.', 'id': 'd08e9748-b1ba-4fd3-9d13-743c1823be72'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '32ee910b-5b89-4b37-a8ae-8843dba9510d', 'book_rating': 4, 'book_review': "The Cherry Orchard is a poignant and tragicomedy that offers a profound commentary on social change and the passage of time. Anton Chekhov's characters are richly drawn, and his dialogue is sharp and insightful.", 'short_review': 'Poignant tragicomedy.', 'id': 'c5d2f894-f5a4-4862-a7ea-898acb3da2cb'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': '32ee910b-5b89-4b37-a8ae-8843dba9510d', 'book_rating': 5, 'book_review': "The Cherry Orchard is a masterpiece of Russian literature. Chekhov's exploration of themes such as class, change, and loss is both profound and timeless. A must-read for anyone interested in drama.", 'short_review': 'Masterpiece of Russian literature.', 'id': '0d78df78-3077-40fc-91a4-3a990705bc06'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': '32ee910b-5b89-4b37-a8ae-8843dba9510d', 'book_rating': 3, 'book_review': "While The Cherry Orchard has moments of brilliance, I found some parts of the play to be slow and meandering. However, Chekhov's keen observation of human nature shines through, making it worth the read.", 'short_review': 'Moments of brilliance.', 'id': '3df800d0-d0ed-4e28-969c-cc733a5dc550'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': 'aab4e42b-f568-4b36-9625-fcdbcec3151d', 'book_rating': 4, 'book_review': "The Age of Innocence is a captivating novel that provides a vivid portrayal of New York society in the late 19th century. Edith Wharton's prose is elegant and her characters are intricately developed.", 'short_review': 'Captivating portrayal.', 'id': 'bf5731f6-3c85-4c5d-8ad3-d42ff58b5f04'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': 'aab4e42b-f568-4b36-9625-fcdbcec3151d', 'book_rating': 5, 'book_review': "The Age of Innocence is a masterpiece of American literature. Wharton's exploration of love, duty, and societal expectations is both timeless and thought-provoking.", 'short_review': 'Masterpiece of literature.', 'id': '0d434a33-5e2b-48e8-8190-ef2169898865'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': 'cf407f4a-2a5d-4caa-ac4f-a2e88d626295', 'book_rating': 3, 'book_review': "In Search of Lost Time is a monumental work that delves into the intricacies of memory, time, and identity. Marcel Proust's prose is dense and philosophical, requiring patience and reflection.", 'short_review': 'Monumental work.', 'id': 'cd92998f-961b-46cb-8d9d-2daab811e74d'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': 'cf407f4a-2a5d-4caa-ac4f-a2e88d626295', 'book_rating': 2, 'book_review': "In Search of Lost Time is a challenging read due to its length and dense prose. While Proust's exploration of memory is profound, the narrative can be slow-paced and meandering.", 'short_review': 'Challenging read.', 'id': '507b01b8-fd89-4fe5-ab44-c4b59aa75f63'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'e8cecd24-15d5-4395-bf73-2dbdd8c79d6e', 'book_rating': 5, 'book_review': "The Waste Land is a groundbreaking poem that captures the disillusionment and fragmentation of the post-World War I era. T.S. Eliot's use of imagery and symbolism is masterful, making this poem a seminal work of modernist literature.", 'short_review': 'Groundbreaking poem.', 'id': '7d3ca9aa-3ec9-401f-b8dd-bf182201556d'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'e8cecd24-15d5-4395-bf73-2dbdd8c79d6e', 'book_rating': 4, 'book_review': "The Waste Land is a complex and thought-provoking poem that requires multiple readings to fully appreciate. Eliot's use of literary allusions and fragmented structure adds layers of meaning to the text.", 'short_review': 'Thought-provoking poem.', 'id': '2d9d9844-c004-4a96-930f-962d1e7d145b'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '4011081b-fe69-48fc-b938-1b4afeb61d0a', 'book_rating': 4, 'book_review': "The Stranger is a compelling existential novel that challenges conventional notions of morality and identity. Albert Camus's sparse prose and detached narration create an atmosphere of absurdity and alienation.", 'short_review': 'Compelling existential novel.', 'id': 'ff0e4c4d-fdef-4372-9edd-2b34223a38ac'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '4011081b-fe69-48fc-b938-1b4afeb61d0a', 'book_rating': 3, 'book_review': "While The Stranger offers an interesting exploration of existential themes, I found the protagonist's detachment to be off-putting at times. However, Camus's writing style is undeniably impactful.", 'short_review': 'Interesting exploration.', 'id': '2d462dbf-cd57-416d-ad99-0cba6d5bc5a8'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '588a4ec6-e7bd-451d-bfb6-44460683bb10', 'book_rating': 4, 'book_review': "Waiting for Godot is a thought-provoking play that explores themes of existentialism and the human condition. Samuel Beckett's minimalist style and absurdist dialogue create a unique theatrical experience.", 'short_review': 'Thought-provoking play.', 'id': '37a7cafa-08e4-4db3-877c-7c42cc0e5696'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '588a4ec6-e7bd-451d-bfb6-44460683bb10', 'book_rating': 5, 'book_review': "Waiting for Godot is a masterpiece of modern theater. Beckett's exploration of the futility of human existence is both profound and darkly humorous. A must-read for anyone interested in existentialist literature.", 'short_review': 'Masterpiece of theater.', 'id': 'b130ff7e-a5de-4e49-bdf4-c8857e743c3c'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '755dcd0e-9ed8-4879-8f69-9474e246d7ed', 'book_rating': 3, 'book_review': "On the Road is a classic novel that captures the spirit of the Beat Generation. Jack Kerouac's spontaneous prose and vivid descriptions of the American landscape make this a compelling read, although the lack of a cohesive plot may deter some readers.", 'short_review': 'Captures the Beat spirit.', 'id': '8490425c-c907-423e-9a7e-ca9c728e3512'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '755dcd0e-9ed8-4879-8f69-9474e246d7ed', 'book_rating': 2, 'book_review': "On the Road is an overrated novel that glorifies aimless wanderlust. While Kerouac's prose captures the spontaneity of the Beat Generation, the lack of character development and coherent plot make it a frustrating read.", 'short_review': 'Overrated wanderlust.', 'id': '4e82ef6d-a02f-46a3-8fe6-4773621f884f'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '105a4621-d03d-46d9-a297-9f7e08f68c96', 'book_rating': 4, 'book_review': "Naked Lunch is a challenging yet rewarding novel that pushes the boundaries of traditional narrative structure. William S. Burroughs's surrealistic prose and vivid imagery create a disturbing but fascinating exploration of addiction and alienation.", 'short_review': 'Challenging but rewarding.', 'id': '309f4a83-9f81-41b2-a0d0-31098aa7c0ab'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '105a4621-d03d-46d9-a297-9f7e08f68c96', 'book_rating': 5, 'book_review': "Naked Lunch is a groundbreaking work of literature that defies categorization. Burroughs's stream-of-consciousness style and surrealistic imagery create a hallucinatory experience that challenges the reader's perceptions.", 'short_review': 'Groundbreaking literature.', 'id': '51d98bca-fda7-4f3a-ba26-52d561214886'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '308c5307-f281-4d97-914f-d73529f1c436', 'book_rating': 5, 'book_review': "Atonement is a beautifully written novel that explores the complexities of guilt, forgiveness, and redemption. Ian McEwan's prose is elegant and evocative, drawing the reader into the lives of the characters and their interconnected stories.", 'short_review': 'Beautifully written.', 'id': 'd43e4794-1d99-45c2-bbb0-3dc6bd4444ee'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '308c5307-f281-4d97-914f-d73529f1c436', 'book_rating': 4, 'book_review': "Atonement is a captivating novel that explores the consequences of a single lie. McEwan's masterful storytelling and rich character development make this a compelling read from start to finish.", 'short_review': 'Captivating story.', 'id': '24bc4c6f-40ba-47e5-8d1d-5238b2f58b03'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'ec9bf649-1ad2-41eb-b264-bd10c80687ee', 'book_rating': 3, 'book_review': 'The English Patient is a well-written novel with beautiful prose and vivid descriptions of wartime Europe. However, the nonlinear narrative structure may confuse some readers and detract from the overall enjoyment of the story.', 'short_review': 'Well-written but confusing.', 'id': 'b365d0e1-b7ab-40fc-8fe9-4f03b1f4c81a'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'a2663654-96bf-44f4-8285-01f8d61a2193', 'book_rating': 5, 'book_review': "The Sense of an Ending is a thought-provoking and introspective novel that explores memory, identity, and the passage of time. Julian Barnes's writing is sharp and insightful, leaving a lasting impression on the reader.", 'short_review': 'Thought-provoking.', 'id': '4cb12205-c449-43a5-9214-454b44ccd8f2'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '144c7663-377a-42b2-a074-578a1e32cb8d', 'book_rating': 4, 'book_review': "The Unbearable Lightness of Being is a philosophical novel that delves into the complexities of love, identity, and existence. Milan Kundera's writing style is both poetic and thought-provoking, making this a compelling read for those who enjoy introspective literature.", 'short_review': 'Poetic and thought-provoking.', 'id': '41bec4ff-69e9-4735-8971-405eb3f3b9ed'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '179fcde5-031d-401c-99e1-75d7858c1668', 'book_rating': 2, 'book_review': 'Infinite Jest is a challenging and ambitious novel that explores various themes such as addiction, entertainment, and the search for meaning. However, its nonlinear narrative structure and extensive footnotes may deter some readers from fully engaging with the story.', 'short_review': 'Challenging but not engaging.', 'id': 'ea906cbf-766b-4e24-a3da-2505c0dc7c29'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '4d4915f8-ef78-482b-a865-7f31ab798c9a', 'book_rating': 5, 'book_review': "The Tale of Genji is a masterpiece of Japanese literature, offering a fascinating glimpse into the courtly life of Heian-era Japan. Murasaki Shikibu's vivid descriptions and intricate characterizations make this epic tale a timeless classic that continues to captivate readers centuries after its initial publication.", 'short_review': 'Timeless classic.', 'id': 'f620e771-da0c-42cb-b6f2-7f7ac5b94076'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '4d4915f8-ef78-482b-a865-7f31ab798c9a', 'book_rating': 4, 'book_review': "The Tale of Genji is a rich and immersive reading experience that transports readers to a different time and place. Murasaki Shikibu's narrative skill and attention to detail bring the characters and settings to life, making it a must-read for fans of classic literature.", 'short_review': 'Rich and immersive.', 'id': '508b551f-b344-429d-af4e-e6ef2038197c'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '92bbd1f2-069b-4828-bd02-6f6afe3de195', 'book_rating': 4, 'book_review': "A Room with a View is a delightful novel that explores themes of love, social class, and freedom. E.M. Forster's writing is both charming and insightful, making this book a timeless classic that continues to resonate with readers today.", 'short_review': 'Charming and insightful.', 'id': 'f865234b-f71c-4560-887d-ce589b96ab52'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': 'f6634faa-4159-41a0-9d6e-20f3d51a27f7', 'book_rating': 3, 'book_review': "The End of the Affair is a poignant exploration of love, loss, and redemption. Graham Greene's writing is evocative and thought-provoking, but some readers may find the pacing slow and the plot predictable.", 'short_review': 'Poignant but slow pacing.', 'id': '37f23a2f-fb9d-46aa-8db8-79ee0ec714d5'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'cdcadae9-09a4-4820-892a-8a2e28f35ddb', 'book_rating': 5, 'book_review': "Henderson the Rain King is a wild and whimsical adventure that defies categorization. Saul Bellow's vivid prose and eccentric characters make this novel a captivating read from start to finish.", 'short_review': 'Wild and whimsical.', 'id': '164ae1a8-eaf4-4cc0-a5b0-c7b1a610b433'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '92bbd1f2-069b-4828-bd02-6f6afe3de195', 'book_rating': 4, 'book_review': "A Room with a View is a beautifully written novel that transports readers to the idyllic landscapes of Italy. E.M. Forster's exploration of romance and societal expectations is both poignant and thought-provoking.", 'short_review': 'Beautifully written.', 'id': 'efa2b0bb-5317-428d-bb37-963ce49ca717'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '37d2da2f-1a3b-4a01-ab38-162100a833af', 'book_rating': 4, 'book_review': "A Good Man Is Hard to Find is a gripping collection of short stories that delves into the complexities of human nature. Flannery O'Connor's writing is both haunting and insightful, leaving a lasting impression on readers.", 'short_review': 'Haunting and insightful.', 'id': 'f09d5918-bc40-4eec-9b5c-17fe4e667c96'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '37d2da2f-1a3b-4a01-ab38-162100a833af', 'book_rating': 3, 'book_review': "A Good Man Is Hard to Find offers a glimpse into the darker aspects of life through its intriguing characters and unexpected plot twists. While some stories are more engaging than others, Flannery O'Connor's masterful storytelling shines throughout.", 'short_review': 'Engaging but uneven.', 'id': '01cb3075-f8db-4bdb-af14-38d5ab831f4c'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '37d2da2f-1a3b-4a01-ab38-162100a833af', 'book_rating': 5, 'book_review': "A Good Man Is Hard to Find is a literary masterpiece that skillfully blends elements of humor, tragedy, and morality. Flannery O'Connor's vivid imagery and sharp wit make this collection a must-read for fans of Southern Gothic fiction.", 'short_review': 'Masterful and vivid.', 'id': 'f26c4e70-7429-47fd-a6f4-56d2737541cf'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '17aa4df7-f547-46d4-a60d-ddb68d89ce2d', 'book_rating': 3, 'book_review': "Death of a Naturalist offers a lyrical exploration of nature and childhood memories. Seamus Heaney's poetry is evocative, but some readers may find the themes repetitive.", 'short_review': 'Lyrical but repetitive.', 'id': '850bff04-61b3-4bce-9d9e-ad1e91c7b79f'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '17aa4df7-f547-46d4-a60d-ddb68d89ce2d', 'book_rating': 5, 'book_review': "Death of a Naturalist is a poignant collection of poems that captures the beauty and brutality of the natural world. Seamus Heaney's imagery is vivid, and his exploration of Irish rural life is both captivating and moving.", 'short_review': 'Captivating and moving.', 'id': 'c45147b7-3a9f-4c08-abcd-8b2f6dbcdf11'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '17aa4df7-f547-46d4-a60d-ddb68d89ce2d', 'book_rating': 4, 'book_review': "Death of a Naturalist is a compelling collection of poems that skillfully juxtaposes the beauty and harshness of nature. Seamus Heaney's poetic language transports readers to the Irish countryside, evoking a sense of nostalgia and wonder.", 'short_review': 'Compelling and nostalgic.', 'id': 'ca9c15c3-b7d0-46d9-9704-b43f660a3306'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '61e48b82-ca50-4e17-9b66-7b007eb2218c', 'book_rating': 4, 'book_review': "Omeros is an epic poem that weaves together themes of history, identity, and mythology. Derek Walcott's lyrical prose transports readers to the Caribbean, offering a rich and immersive reading experience.", 'short_review': 'Rich and immersive.', 'id': 'df42cd54-ea69-4c87-9116-e40fec2a542b'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '61e48b82-ca50-4e17-9b66-7b007eb2218c', 'book_rating': 5, 'book_review': "Omeros is a breathtaking work of literature that blends mythology with the harsh realities of Caribbean life. Derek Walcott's poetic language and vivid imagery create a mesmerizing narrative that stays with the reader long after the final page.", 'short_review': 'Breathtaking and mesmerizing.', 'id': '32d9cdac-e18b-439c-bcc8-b05f74f14a9d'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': '61e48b82-ca50-4e17-9b66-7b007eb2218c', 'book_rating': 3, 'book_review': "Omeros is a complex and ambitious poem that explores themes of identity, colonization, and cultural heritage. While Derek Walcott's writing is undeniably beautiful, the structure of the poem can be difficult to follow at times.", 'short_review': 'Beautiful but challenging.', 'id': '0ca5b7af-166a-43c4-8764-a4062e8eb97f'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': '51fab1f5-e7c9-47fc-965a-15027bb7c2d3', 'book_rating': 4, 'book_review': "The Magic Mountain is a thought-provoking novel that explores complex philosophical ideas within the confines of a sanatorium. Thomas Mann's intricate prose and rich character development make this book a rewarding but challenging read.", 'short_review': 'Thought-provoking and rewarding.', 'id': '87704ffa-8965-4ea9-8801-4852239f1966'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '51fab1f5-e7c9-47fc-965a-15027bb7c2d3', 'book_rating': 5, 'book_review': "The Magic Mountain is an immersive journey into the human psyche, set against the backdrop of a tuberculosis sanatorium. Thomas Mann's prose is dense but rewarding, offering profound insights into life, death, and the search for meaning.", 'short_review': 'Immersive and profound.', 'id': '6f3b4add-09c2-4051-be2f-3dc45d22cc5f'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '51fab1f5-e7c9-47fc-965a-15027bb7c2d3', 'book_rating': 3, 'book_review': "The Magic Mountain is a challenging yet ultimately rewarding novel that delves into the complexities of human existence. While Thomas Mann's philosophical musings can be dense at times, the depth of his insights makes this book a worthwhile read.", 'short_review': 'Challenging but worthwhile.', 'id': '70e6b36c-d05b-4bf1-94e5-e2cbd1c9570a'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': 'd3a4f48f-8243-49e3-8250-452fb38225a1', 'book_rating': 5, 'book_review': "Ficciones is a mesmerizing collection of short stories that showcases Jorge Luis Borges' unparalleled imagination and intellect. Each story is a labyrinth of ideas, inviting readers to explore philosophical concepts and existential dilemmas.", 'short_review': 'Mesmerizing and thought-provoking.', 'id': '466f52dc-5926-43d9-b581-af87547041df'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': 'd3a4f48f-8243-49e3-8250-452fb38225a1', 'book_rating': 4, 'book_review': "Ficciones is a literary masterpiece that blurs the lines between reality and fiction. Jorge Luis Borges' innovative narrative techniques and intricate plots make this collection a must-read for lovers of mind-bending literature.", 'short_review': 'Innovative and mind-bending.', 'id': 'b45bdd95-d5b9-4dab-9e4b-b5abb98b1819'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': 'd3a4f48f-8243-49e3-8250-452fb38225a1', 'book_rating': 3, 'book_review': "Ficciones is an intellectually stimulating collection of stories that challenges readers to question the nature of reality. While Jorge Luis Borges' writing is undeniably brilliant, some stories may feel inaccessible to casual readers.", 'short_review': 'Intellectually stimulating but inaccessible.', 'id': '5ffae82f-47e8-497c-9563-d5a70f6e3bcf'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': 'c78ebd24-9e96-4e84-9843-7016a9602323', 'book_rating': 4, 'book_review': "Invisible Cities is a breathtaking exploration of imagination and urban landscapes. Italo Calvino's prose is lyrical and evocative, painting vivid portraits of imaginary cities that linger in the mind long after the book is finished.", 'short_review': 'Breathtaking and vivid.', 'id': 'fc348907-8426-4e48-8092-7a23179e5cda'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': 'c78ebd24-9e96-4e84-9843-7016a9602323', 'book_rating': 5, 'book_review': "Invisible Cities is a literary marvel that transcends the boundaries of traditional storytelling. Italo Calvino's imaginative vision and poetic language create a mesmerizing journey through fantastical cities that defy logic and convention.", 'short_review': 'Mesmerizing and poetic.', 'id': 'a18d23fc-59b8-48c5-8ac3-f11921b20e84'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': 'c78ebd24-9e96-4e84-9843-7016a9602323', 'book_rating': 3, 'book_review': "Invisible Cities is an ambitious work that showcases Italo Calvino's boundless creativity. While some sections are beautifully crafted, others may feel disjointed or overly abstract, making the reading experience uneven.", 'short_review': 'Ambitious but uneven.', 'id': '21d91cba-901d-4a66-9192-fb9fadb0739d'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '9b5427ed-badb-4e4e-82f3-478ab7d8e0c4', 'book_rating': 4, 'book_review': "Blindness is a haunting exploration of human nature and society's response to crisis. Jose Saramago's stark prose and relentless narrative pull readers into a dystopian world where the loss of sight reveals the darkness within us all.", 'short_review': 'Haunting and relentless.', 'id': 'a0b59ef3-ade0-4ddd-8e62-2a5279789737'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '9b5427ed-badb-4e4e-82f3-478ab7d8e0c4', 'book_rating': 5, 'book_review': "Blindness is a powerful allegory that exposes the fragility of civilization and the resilience of the human spirit. Jose Saramago's unflinching portrayal of societal collapse is both harrowing and thought-provoking, leaving a profound impact on readers.", 'short_review': 'Powerful and thought-provoking.', 'id': 'e7bdc038-c21a-44d3-a238-cb2b8353cd3e'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': '9b5427ed-badb-4e4e-82f3-478ab7d8e0c4', 'book_rating': 3, 'book_review': "Blindness is a disturbing yet compelling novel that explores the darkest depths of human nature. While Jose Saramago's writing is undeniably powerful, the relentless bleakness of the narrative may be overwhelming for some readers.", 'short_review': 'Disturbing but powerful.', 'id': 'a68e6b0d-273d-4e43-a5fe-b81b5ef6d4c4'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': 'fabe6dd1-fa38-457c-9f9d-6676ef7002d6', 'book_rating': 4, 'book_review': "If This Is a Man is a harrowing memoir that offers a stark portrayal of survival and resilience in the face of unimaginable suffering. Primo Levi's unflinching honesty and introspection make this book a haunting testament to the human spirit.", 'short_review': 'Harrowing and honest.', 'id': '4416b61c-253d-41ec-93c3-b58b11db334b'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '507a7709-0beb-4795-8ac8-de908803bbaa', 'book_rating': 5, 'book_review': "The Name of the Rose is a captivating historical mystery that combines elements of theology, philosophy, and suspense. Umberto Eco's meticulous attention to detail and rich character development make this novel a must-read for fans of intelligent fiction.", 'short_review': 'Captivating and intelligent.', 'id': '11746a3c-5256-4b11-8ce3-3c3f829c395c'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '507a7709-0beb-4795-8ac8-de908803bbaa', 'book_rating': 4, 'book_review': "The Name of the Rose is an intriguing blend of historical fiction and murder mystery. Umberto Eco's erudite prose and intricate plot keep readers engaged until the very end, though some may find the theological discussions overwhelming at times.", 'short_review': 'Intriguing but overwhelming.', 'id': 'e620f6ff-ea67-4c2f-97b1-6a29a84cf57e'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': '507a7709-0beb-4795-8ac8-de908803bbaa', 'book_rating': 3, 'book_review': "The Name of the Rose is an ambitious novel that delves deep into the realms of history, religion, and philosophy. While Umberto Eco's prose is undeniably masterful, the dense philosophical discussions may alienate some readers.", 'short_review': 'Ambitious but alienating.', 'id': 'cf7799e0-dc8b-4216-bf35-9b4e5cec7ea9'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': '507a7709-0beb-4795-8ac8-de908803bbaa', 'book_rating': 4, 'book_review': "The Name of the Rose is a thought-provoking novel that challenges readers to explore complex themes of faith, knowledge, and power. Umberto Eco's narrative skill and historical depth create an immersive reading experience that lingers long after the book is finished.", 'short_review': 'Thought-provoking and immersive.', 'id': '2298b107-85fc-4cfc-b428-eaf846a7cb52'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '66eece62-7a93-46a3-85c4-4ba15e646bd0', 'book_rating': 3, 'book_review': "White Teeth is a sprawling epic that navigates themes of identity, culture, and belonging. Zadie Smith's ambitious storytelling and vivid characterizations make this novel a compelling read, although some may find its length and multiple narratives overwhelming.", 'short_review': 'Ambitious but overwhelming.', 'id': '586dd64d-e1b2-4862-924e-e12b4f5c86e5'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '66eece62-7a93-46a3-85c4-4ba15e646bd0', 'book_rating': 4, 'book_review': "White Teeth is a brilliant exploration of multiculturalism and the complexities of modern life. Zadie Smith's sharp wit and keen observation create a vibrant tapestry of characters and stories that resonate with readers from diverse backgrounds.", 'short_review': 'Brilliant and vibrant.', 'id': '14f4c115-f21c-4791-9ec0-cc3cbd2f76e2'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '66eece62-7a93-46a3-85c4-4ba15e646bd0', 'book_rating': 5, 'book_review': "White Teeth is an exhilarating literary journey that captures the essence of multicultural London. Zadie Smith's sharp social commentary and richly drawn characters make this novel a true masterpiece of modern literature.", 'short_review': 'Exhilarating and masterful.', 'id': 'bb994355-89a0-4145-9051-139116b3216e'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '66eece62-7a93-46a3-85c4-4ba15e646bd0', 'book_rating': 3, 'book_review': "White Teeth is a complex and ambitious novel that explores the intricacies of identity and culture. While Zadie Smith's writing is undeniably powerful, the sprawling narrative and multitude of characters may overwhelm some readers.", 'short_review': 'Complex but overwhelming.', 'id': '67924c1e-742d-4783-848f-0213306c448f'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '1e0c4f7a-c46c-4dad-97be-06061010c73a', 'book_rating': 4, 'book_review': "My Brilliant Friend is a captivating exploration of friendship, identity, and societal expectations. Elena Ferrante's richly textured prose and intimate portrayal of female friendship make this novel a poignant and unforgettable read.", 'short_review': 'Captivating and poignant.', 'id': 'fdaee9fe-fda7-495a-b770-e4ea02523d16'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '88814018-1039-4f93-aeac-dda2e321b287', 'book_rating': 5, 'book_review': "The Underground Railroad is a powerful and moving novel that offers a gripping portrayal of the horrors of slavery in America. Colson Whitehead's writing is both haunting and lyrical, making this book a must-read for anyone interested in American history.", 'short_review': 'Powerful and moving.', 'id': '35bf80d4-00f2-420a-ab3d-b62773b59f1a'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': '88814018-1039-4f93-aeac-dda2e321b287', 'book_rating': 4, 'book_review': "The Underground Railroad is a compelling and thought-provoking novel that explores the harsh realities of slavery in America. Colson Whitehead's vivid storytelling and well-developed characters make this book an engrossing read from start to finish.", 'short_review': 'Compelling and thought-provoking.', 'id': 'cb3ded68-6dff-4ebd-a4a6-93382c12cf50'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': '88814018-1039-4f93-aeac-dda2e321b287', 'book_rating': 3, 'book_review': "The Underground Railroad is an important and impactful novel that sheds light on a dark chapter of American history. While Colson Whitehead's prose is undeniably powerful, the nonlinear narrative may be confusing for some readers.", 'short_review': 'Important but confusing.', 'id': 'a124fefe-91be-44d8-a5f7-232ae6f31cbb'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '88814018-1039-4f93-aeac-dda2e321b287', 'book_rating': 5, 'book_review': "The Underground Railroad is a masterfully crafted novel that vividly captures the struggles of enslaved people seeking freedom. Colson Whitehead's storytelling prowess and vivid imagery make this book a profound and unforgettable read.", 'short_review': 'Masterfully crafted and profound.', 'id': 'e8693a9e-2cc7-41f0-b4fc-f7ec9d286aa7'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '980a7310-f81e-4e5f-9cde-ee0a440c0335', 'book_rating': 4, 'book_review': "The Second Sex is a groundbreaking work that remains relevant in its exploration of gender and society. Simone de Beauvoir's thorough analysis and critical insights make this book essential reading for anyone interested in feminist theory.", 'short_review': 'Groundbreaking and relevant.', 'id': '0328e2a2-a296-4b20-a822-8685912e9d07'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '980a7310-f81e-4e5f-9cde-ee0a440c0335', 'book_rating': 3, 'book_review': "The Second Sex offers a comprehensive examination of the status of women in society, but its dense philosophical prose may be challenging for some readers to digest. Simone de Beauvoir's insights, however, are invaluable for understanding the complexities of gender.", 'short_review': 'Comprehensive but challenging.', 'id': '28bde212-5528-4d53-8ff4-c0388b03e3a4'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '980a7310-f81e-4e5f-9cde-ee0a440c0335', 'book_rating': 5, 'book_review': "The Second Sex is an essential feminist text that offers a profound analysis of the oppression of women throughout history. Simone de Beauvoir's eloquent prose and incisive critique make this book a timeless classic that continues to inspire generations of readers.", 'short_review': 'Essential and timeless.', 'id': '23a675c5-08ff-4dee-9fc5-71ad1210f739'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '4f7ceba9-7c72-44dc-8e18-28b2fc3a4553', 'book_rating': 4, 'book_review': "Charlie and the Chocolate Factory is a delightful and whimsical tale that sparks the imagination. Roald Dahl's colorful characters and imaginative world-building make this book a timeless classic for readers of all ages.", 'short_review': 'Delightful and whimsical.', 'id': '26474bff-82fe-4fad-a44a-ee0c8611575e'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': 'cac758ad-3381-4182-a6ea-0022b083495a', 'book_rating': 4, 'book_review': "The Talented Mr. Ripley is a gripping psychological thriller that keeps you on the edge of your seat. Patricia Highsmith's masterful storytelling and complex characters make this book a must-read for fans of the genre.", 'short_review': 'Gripping and masterful.', 'id': '781dac89-a557-4b31-92ac-0a69fe716315'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': 'cac758ad-3381-4182-a6ea-0022b083495a', 'book_rating': 3, 'book_review': "The Talented Mr. Ripley is an intriguing novel with a unique premise, but the pacing may feel slow for some readers. Patricia Highsmith's exploration of identity and morality, however, is thought-provoking.", 'short_review': 'Intriguing but slow-paced.', 'id': '4fad9f3f-2d54-4fbb-8874-4283439da87b'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': 'cac758ad-3381-4182-a6ea-0022b083495a', 'book_rating': 5, 'book_review': "The Talented Mr. Ripley is a masterpiece of suspense and psychological tension. Patricia Highsmith's portrayal of Tom Ripley's descent into amorality is both chilling and captivating, making this book an unforgettable read.", 'short_review': 'Masterpiece of suspense.', 'id': 'e66d8709-55a1-4a62-9ea3-84b14abafa2c'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': 'cac758ad-3381-4182-a6ea-0022b083495a', 'book_rating': 4, 'book_review': "The Talented Mr. Ripley is a riveting and unsettling thriller that delves into the depths of human nature. Patricia Highsmith's exploration of obsession and deception is as thought-provoking as it is chilling.", 'short_review': 'Riveting and unsettling.', 'id': 'b27227b3-b8d8-4ea3-a083-bec8501e7b40'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': '744ebc9e-f9bc-436e-8fbc-358b21caf417', 'book_rating': 5, 'book_review': "Night is a powerful and haunting memoir that offers a firsthand account of the horrors of the Holocaust. Elie Wiesel's prose is both eloquent and deeply moving, making this book an essential read for understanding the human experience during wartime.", 'short_review': 'Powerful and haunting.', 'id': 'ccc77deb-1388-4add-99d4-925fdc6282e0'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '744ebc9e-f9bc-436e-8fbc-358b21caf417', 'book_rating': 4, 'book_review': "Night is a harrowing and unforgettable memoir that vividly captures the atrocities of the Holocaust. Elie Wiesel's firsthand account of survival and loss serves as a stark reminder of the resilience of the human spirit.", 'short_review': 'Harrowing and unforgettable.', 'id': '99ed6abf-2979-45ce-9e45-8edb1f0866df'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': 'bcbec230-2e3f-42fc-86ad-77888be36f86', 'book_rating': 3, 'book_review': "Where the Wild Things Are is a whimsical and imaginative children's book that sparks the imagination. Maurice Sendak's illustrations are charming, but the story may be too simplistic for older readers.", 'short_review': 'Whimsical but simplistic.', 'id': '8c27a4f9-af30-454c-aa9f-47b575b758c4'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'bcbec230-2e3f-42fc-86ad-77888be36f86', 'book_rating': 5, 'book_review': "Where the Wild Things Are is a timeless classic that celebrates the power of imagination. Maurice Sendak's whimsical illustrations and heartfelt story resonate with readers of all ages, making this book a beloved favorite.", 'short_review': 'Timeless classic.', 'id': '6c61b5e2-3eba-42ce-bd23-6e02b134d65f'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '13e2d36c-fca8-4efc-8612-d12bd473c31c', 'book_rating': 5, 'book_review': "In the Night Kitchen is a delightful children's book with stunning illustrations and a whimsical storyline. Maurice Sendak's creativity shines through in this imaginative tale that captures the magic of childhood.", 'short_review': 'Delightful and imaginative.', 'id': 'c49a0239-03e3-45d9-877d-d969250becb9'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': '13e2d36c-fca8-4efc-8612-d12bd473c31c', 'book_rating': 4, 'book_review': "In the Night Kitchen is a charming book that sparks the imagination and encourages creativity. Maurice Sendak's illustrations are captivating, and the story is both entertaining and educational.", 'short_review': 'Charming and captivating.', 'id': 'f56e4706-bfcf-4e8e-8366-2547b0446eca'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '13e2d36c-fca8-4efc-8612-d12bd473c31c', 'book_rating': 3, 'book_review': "In the Night Kitchen is an interesting book with unique illustrations, but the storyline may be confusing for young readers. Maurice Sendak's creativity is evident, but the execution falls short in some aspects.", 'short_review': 'Interesting but confusing.', 'id': '5f71bb51-75ad-4292-aa9c-c1a5620e7d5d'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '13e2d36c-fca8-4efc-8612-d12bd473c31c', 'book_rating': 5, 'book_review': "In the Night Kitchen is a classic children's book that stands the test of time. Maurice Sendak's imaginative storytelling and vibrant illustrations make this book a must-read for children of all ages.", 'short_review': 'Classic and vibrant.', 'id': 'a7da365a-64d1-44b6-8359-15de2e5a50ac'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '53e2bf04-958a-49c4-a21a-191a3e8a5e1d', 'book_rating': 5, 'book_review': "The Giving Tree is a heartwarming story that teaches valuable lessons about selflessness and generosity. Shel Silverstein's simple yet profound tale resonates with readers of all ages, making it a timeless classic.", 'short_review': 'Heartwarming and profound.', 'id': 'c6fbc565-29e4-4949-a24e-b04814c94cd3'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '53e2bf04-958a-49c4-a21a-191a3e8a5e1d', 'book_rating': 4, 'book_review': "The Giving Tree is a touching story that explores themes of love and sacrifice. Shel Silverstein's poignant illustrations and simple prose make this book a memorable read for both children and adults.", 'short_review': 'Touching and memorable.', 'id': '9c21d355-5e97-459e-82cd-29084ea451a1'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '53e2bf04-958a-49c4-a21a-191a3e8a5e1d', 'book_rating': 3, 'book_review': "The Giving Tree is a bittersweet story with beautiful illustrations, but the narrative may feel overly simplistic for adult readers. Shel Silverstein's message of selflessness is clear, but the execution lacks depth.", 'short_review': 'Bittersweet with beautiful illustrations.', 'id': 'e82396e7-a298-490c-ac2e-ae4d1e3fb117'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '048fe0a4-b73f-41b0-8c70-e82c7dd9c401', 'book_rating': 4, 'book_review': "Where the Sidewalk Ends is a whimsical collection of poems that delights readers with its imaginative language and playful illustrations. Shel Silverstein's wit and charm shine through in each poem, making this book a joy to read.", 'short_review': 'Whimsical and delightful.', 'id': '742aa735-3154-49b1-9451-870ef3edb2ed'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': '048fe0a4-b73f-41b0-8c70-e82c7dd9c401', 'book_rating': 5, 'book_review': "Where the Sidewalk Ends is a timeless classic that sparks the imagination and encourages creativity in readers of all ages. Shel Silverstein's whimsical poems and illustrations captivate the heart and mind, making this book a beloved favorite.", 'short_review': 'Timeless classic.', 'id': 'e34c43a6-0188-477a-90f7-774210f5a05c'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '55f429ca-96a2-4824-9d4c-cdbe1d0fee8a', 'book_rating': 4, 'book_review': "The Angel's Game is a captivating thriller with intricate plot twists and well-developed characters. Carlos Ruiz Zaf�n's storytelling keeps readers on the edge of their seats until the very end.", 'short_review': 'Captivating thriller.', 'id': '5017ce46-8e08-48d2-906d-c708481af95c'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '55f429ca-96a2-4824-9d4c-cdbe1d0fee8a', 'book_rating': 5, 'book_review': "The Angel's Game is a masterpiece of suspense and mystery. Carlos Ruiz Zaf�n's writing is mesmerizing, and the story unfolds with unexpected twists and turns that keep readers guessing until the end.", 'short_review': 'Masterpiece of suspense.', 'id': '396c6d07-fe26-48be-a1b0-865b3b8922ec'},
    {'user_id': '7c7a29c9-a713-440b-9b85-eb5033f02641', 'book_id': '55f429ca-96a2-4824-9d4c-cdbe1d0fee8a', 'book_rating': 3, 'book_review': "The Angel's Game is an intriguing novel with a complex plot and vivid imagery. While the story keeps readers engaged, some may find the pacing slow at times.", 'short_review': 'Intriguing but slow-paced.', 'id': '816dbc26-3373-420d-85ac-ef89fe317e67'},
    {'user_id': 'ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e', 'book_id': '55f429ca-96a2-4824-9d4c-cdbe1d0fee8a', 'book_rating': 4, 'book_review': "The Angel's Game is a compelling read that immerses readers into a world of mystery and intrigue. Carlos Ruiz Zaf�n's descriptive prose and intricate plot make this book a must-read for fans of suspense.", 'short_review': 'Compelling and immersive.', 'id': '18b230a2-a13a-4a6e-bcc1-ab9c54b966c1'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': 'db373c49-8d18-4e2c-83a4-8d174decd087', 'book_rating': 2, 'book_review': 'The Da Vinci Code is an overrated novel that fails to live up to its hype. While the premise is intriguing, the execution feels contrived, and the writing lacks depth.', 'short_review': 'Overrated and contrived.', 'id': 'ad42c17c-5767-4d18-8eaa-e749c0e0b78b'},
    {'user_id': '9c1b9d38-b2df-4a79-8091-8ef8fa821c88', 'book_id': 'db373c49-8d18-4e2c-83a4-8d174decd087', 'book_rating': 3, 'book_review': "The Da Vinci Code is an entertaining thriller that keeps readers engaged with its fast-paced plot and historical mysteries. While not groundbreaking, it's a decent read for fans of the genre.", 'short_review': 'Entertaining but not groundbreaking.', 'id': 'e9435c1f-b292-49e8-b4c1-2575b09a9f19'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': 'db373c49-8d18-4e2c-83a4-8d174decd087', 'book_rating': 4, 'book_review': "The Da Vinci Code is a gripping page-turner that seamlessly blends history, religion, and conspiracy. Dan Brown's storytelling keeps readers hooked from start to finish, making it a thrilling read.", 'short_review': 'Gripping page-turner.', 'id': '31038a1a-393e-4581-8a77-c666200c79a1'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': 'db373c49-8d18-4e2c-83a4-8d174decd087', 'book_rating': 5, 'book_review': "The Da Vinci Code is a riveting adventure that combines mystery, history, and suspense seamlessly. Dan Brown's storytelling prowess shines in this thrilling tale that keeps readers guessing until the very end.", 'short_review': 'Riveting adventure.', 'id': 'bbc3f0db-6526-4756-a366-6d8d304c6a1a'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': 'dca253be-4e17-4028-ab11-85fb94f33e98', 'book_rating': 4, 'book_review': "Angels & Demons is a fast-paced thriller that keeps readers on the edge of their seats. Dan Brown's intricate plot and suspenseful writing make this book a thrilling ride from start to finish.", 'short_review': 'Fast-paced thriller.', 'id': 'e52b37e7-b3c5-412a-9aac-d20d3a6a2eba'},
    {'user_id': '8410ebc7-bddd-4cff-a651-24b74f193192', 'book_id': '7b122235-11f9-41f2-80e7-da776e1813f2', 'book_rating': 5, 'book_review': "The Dutch House is a beautifully written novel that explores themes of family, loss, and resilience. Ann Patchett's storytelling draws readers into the lives of the characters, making it a compelling and emotional read.", 'short_review': 'Beautifully written.', 'id': '4a4e9818-e7cb-42b8-a9f4-e5b54b492f14'},
    {'user_id': '550de341-e5c4-486f-b087-5ef77ff3a72b', 'book_id': '7b122235-11f9-41f2-80e7-da776e1813f2', 'book_rating': 4, 'book_review': "The Dutch House is a poignant story about the complexities of family dynamics. Ann Patchett's prose is elegant and evocative, creating a richly immersive reading experience.", 'short_review': 'Poignant and immersive.', 'id': '63827237-f01a-488b-a759-f6bc343672d6'},
    {'user_id': '671b88b5-2cb1-43ff-9b2d-c19c6e319ef7', 'book_id': '7b122235-11f9-41f2-80e7-da776e1813f2', 'book_rating': 3, 'book_review': 'The Dutch House offers a nuanced portrayal of familial relationships and their lasting impact. While the writing is skillful, the pacing may feel slow for some readers.', 'short_review': 'Nuanced portrayal.', 'id': '55992e91-1511-4257-ba96-94fdf6281a2b'},
    {'user_id': '7bb8095f-c1a8-4307-b74f-2affe40bae4b', 'book_id': '7b122235-11f9-41f2-80e7-da776e1813f2', 'book_rating': 5, 'book_review': "The Dutch House is a masterfully crafted novel that delves deep into the complexities of human emotion. Ann Patchett's prose is both elegant and moving, making it a truly unforgettable read.", 'short_review': 'Masterfully crafted.', 'id': '60e1f64d-36c2-4e4b-8c5e-d0539f6897da'},
    {'user_id': '3e4992a5-bde8-4df2-ae06-051d0b7a1805', 'book_id': '46016ef3-cc7c-4439-9aec-580fddc43a58', 'book_rating': 2, 'book_review': 'Commonwealth is a disappointing read with underdeveloped characters and a disjointed narrative. While the premise had potential, the execution fell short of expectations.', 'short_review': 'Disappointing and underdeveloped.', 'id': 'ae24ece9-db76-4895-b381-a0b95f576957'},
    {'user_id': '85e505f3-d55e-45cb-8d38-f91ae9164d17', 'book_id': '46016ef3-cc7c-4439-9aec-580fddc43a58', 'book_rating': 3, 'book_review': 'Commonwealth is an interesting exploration of family dynamics and secrets. While the storytelling is engaging, some may find the nonlinear narrative confusing.', 'short_review': 'Engaging but confusing.', 'id': '56731d6f-d696-4767-83bb-092b690b1d32'},
    {'user_id': 'de223b1f-28ef-4921-b846-0613747e1cee', 'book_id': '46016ef3-cc7c-4439-9aec-580fddc43a58', 'book_rating': 4, 'book_review': "Commonwealth is a thought-provoking novel that skillfully weaves together multiple perspectives and timelines. Ann Patchett's storytelling prowess shines in this captivating exploration of family and forgiveness.", 'short_review': 'Thought-provoking and captivating.', 'id': '449217ef-dc51-4ddb-9365-3a7228213cae'},
]





# reviews_data =[
#   {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "94214347-e2c1-4fa4-872f-2b02dfaccfef",
#     "book_rating": 5,
#     "book_review": "The Alchemist is an incredible journey of self-discovery and following one's dreams. Highly recommend it!",
#     "short_review": "Incredible journey!"
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "4e693a90-d582-421b-afbf-a4babf10a68e",
#     "book_rating": 3,
#     "book_review": "Pride and Prejudice is a classic romance with memorable characters. However, I found some parts to be a bit slow.",
#     "short_review": "Classic romance."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "94214347-e2c1-4fa4-872f-2b02dfaccfef",
#     "book_rating": 4,
#     "book_review": "The Alchemist is a thought-provoking book that teaches valuable life lessons. It's definitely worth reading.",
#     "short_review": "Thought-provoking!"
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "4e693a90-d582-421b-afbf-a4babf10a68e",
#     "book_rating": 2,
#     "book_review": "Pride and Prejudice was not my cup of tea. I found it to be overly dramatic and lacking depth in character development.",
#     "short_review": "Not my cup of tea."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "94214347-e2c1-4fa4-872f-2b02dfaccfef",
#     "book_rating": 5,
#     "book_review": "The Alchemist is a masterpiece! It's beautifully written and deeply moving. A must-read for everyone!",
#     "short_review": "A masterpiece!"
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "4e693a90-d582-421b-afbf-a4babf10a68e",
#     "book_rating": 4,
#     "book_review": "Pride and Prejudice is a charming novel with witty dialogue and engaging characters. I thoroughly enjoyed reading it.",
#     "short_review": "Charming novel."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "94214347-e2c1-4fa4-872f-2b02dfaccfef",
#     "book_rating": 3,
#     "book_review": "The Alchemist has some good moments, but overall, I found it to be a bit too preachy for my taste.",
#     "short_review": "Bit too preachy."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "4e693a90-d582-421b-afbf-a4babf10a68e",
#     "book_rating": 5,
#     "book_review": "Pride and Prejudice is a timeless classic that never fails to charm readers with its wit and romance. A must-read for any book lover!",
#     "short_review": "Timeless classic!"
#   },
#   {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "5868f357-1e51-4383-a603-b21dd5881b18",
#     "book_rating": 4,
#     "book_review": "The Adventures of Huckleberry Finn is a classic adventure tale with memorable characters and exciting escapades. Highly recommend it!",
#     "short_review": "Classic adventure!"
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "cb16b8cd-82b2-4489-9a7f-7e085051a001",
#     "book_rating": 3,
#     "book_review": "Mrs. Dalloway is a thought-provoking novel that explores the complexities of human consciousness. Worth reading for its literary merit.",
#     "short_review": "Thought-provoking."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "5868f357-1e51-4383-a603-b21dd5881b18",
#     "book_rating": 5,
#     "book_review": "The Adventures of Huckleberry Finn is an absolute delight to read! Twain's storytelling prowess shines through every page.",
#     "short_review": "Absolute delight!"
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "cb16b8cd-82b2-4489-9a7f-7e085051a001",
#     "book_rating": 2,
#     "book_review": "Mrs. Dalloway was not my cup of tea. I found the stream of consciousness style confusing and hard to follow.",
#     "short_review": "Not my cup of tea."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "5868f357-1e51-4383-a603-b21dd5881b18",
#     "book_rating": 4,
#     "book_review": "The Adventures of Huckleberry Finn is a timeless classic that never fails to entertain. Twain's wit and humor make it a joy to read.",
#     "short_review": "Timeless classic!"
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "cb16b8cd-82b2-4489-9a7f-7e085051a001",
#     "book_rating": 5,
#     "book_review": "Mrs. Dalloway is a masterpiece of modernist literature. Woolf's portrayal of consciousness is both innovative and captivating.",
#     "short_review": "Modernist masterpiece!"
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "5868f357-1e51-4383-a603-b21dd5881b18",
#     "book_rating": 3,
#     "book_review": "The Adventures of Huckleberry Finn was a decent read. While some parts were engaging, others felt slow and dragged on.",
#     "short_review": "Decent read."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "cb16b8cd-82b2-4489-9a7f-7e085051a001",
#     "book_rating": 4,
#     "book_review": "Mrs. Dalloway is a beautifully written novel that offers profound insights into the human psyche. Woolf's prose is exquisite.",
#     "short_review": "Beautifully written."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "81b45f95-dd8b-40b9-a4ef-3754963d5f7a",
#     "book_rating": 5,
#     "book_review": "Anna Karenina is a timeless masterpiece that delves deep into the complexities of love and society. Tolstoy's characters are richly developed, and the narrative is beautifully crafted.",
#     "short_review": "Timeless masterpiece!"
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "6e515ee5-0529-4013-ad25-5c3c5f4d79b1",
#     "book_rating": 3,
#     "book_review": "Warrior of the Light offers some inspiring insights, but overall, I found it to be a bit repetitive. The message is uplifting, but it could have been conveyed more effectively.",
#     "short_review": "Inspiring but repetitive."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "81b45f95-dd8b-40b9-a4ef-3754963d5f7a",
#     "book_rating": 4,
#     "book_review": "Anna Karenina is a powerful exploration of human emotions and desires. Tolstoy's storytelling prowess shines through every page, making it a compelling read.",
#     "short_review": "Powerful exploration."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "6e515ee5-0529-4013-ad25-5c3c5f4d79b1",
#     "book_rating": 2,
#     "book_review": "Warrior of the Light was a disappointment for me. I expected more profound wisdom, but it felt shallow and cliché. Not worth the hype.",
#     "short_review": "Disappointing."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "81b45f95-dd8b-40b9-a4ef-3754963d5f7a",
#     "book_rating": 5,
#     "book_review": "Anna Karenina is an absolute gem of literature! Tolstoy's ability to capture the human condition is unparalleled. A must-read for any book lover.",
#     "short_review": "Absolute gem!"
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "6e515ee5-0529-4013-ad25-5c3c5f4d79b1",
#     "book_rating": 4,
#     "book_review": "Warrior of the Light provides some valuable life lessons and motivational quotes. It's a quick read that can uplift your spirits when needed.",
#     "short_review": "Valuable life lessons."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "81b45f95-dd8b-40b9-a4ef-3754963d5f7a",
#     "book_rating": 3,
#     "book_review": "Anna Karenina was a bit of a mixed bag for me. While I appreciated the depth of the characters, I found the plot to be overly complex and meandering.",
#     "short_review": "Mixed bag."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "6e515ee5-0529-4013-ad25-5c3c5f4d79b1",
#     "book_rating": 5,
#     "book_review": "Warrior of the Light is a beacon of hope in the darkness. Its messages of perseverance and courage are exactly what I needed to hear. Highly recommend it!",
#     "short_review": "Beacon of hope!"
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "efdd1fbe-91bb-4e26-9709-30c863b41cec",
#     "book_rating": 4,
#     "book_review": "Emma is a delightful read with charming characters and witty dialogue. Austen's writing style is captivating, making it a classic.",
#     "short_review": "Delightful read!"
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "ae30fc90-3b04-48b1-b3a9-eedabe83457c",
#     "book_rating": 3,
#     "book_review": "Life on the Mississippi provides an interesting glimpse into the life along the river. Twain's anecdotes are amusing, but the narrative feels a bit disjointed.",
#     "short_review": "Interesting glimpse."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "efdd1fbe-91bb-4e26-9709-30c863b41cec",
#     "book_rating": 5,
#     "book_review": "Emma is an absolute masterpiece! Austen's portrayal of society and romance is unparalleled. A must-read for any literature enthusiast.",
#     "short_review": "Absolute masterpiece!"
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "ae30fc90-3b04-48b1-b3a9-eedabe83457c",
#     "book_rating": 2,
#     "book_review": "Life on the Mississippi was a disappointment for me. I expected more engaging storytelling, but it felt tedious and overly descriptive.",
#     "short_review": "Disappointing."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "efdd1fbe-91bb-4e26-9709-30c863b41cec",
#     "book_rating": 4,
#     "book_review": "Emma is a classic novel with timeless themes of love, friendship, and self-discovery. Austen's characters are vividly drawn, and the plot is engaging.",
#     "short_review": "Timeless themes."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "ae30fc90-3b04-48b1-b3a9-eedabe83457c",
#     "book_rating": 4,
#     "book_review": "Life on the Mississippi offers a fascinating look at the river and the people who inhabit its shores. Twain's wit shines through, making it an enjoyable read.",
#     "short_review": "Fascinating look."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "efdd1fbe-91bb-4e26-9709-30c863b41cec",
#     "book_rating": 3,
#     "book_review": "Emma was an okay read for me. While I appreciated Austen's wit, I found some parts to be a bit slow-paced.",
#     "short_review": "Okay read."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "ae30fc90-3b04-48b1-b3a9-eedabe83457c",
#     "book_rating": 5,
#     "book_review": "Life on the Mississippi is a fascinating blend of history, humor, and adventure. Twain's observations are sharp and his storytelling is engaging. Highly recommend it!",
#     "short_review": "Fascinating blend!"
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "4bad32a8-6fba-4f3e-bff5-68d675149a9b",
#     "book_rating": 5,
#     "book_review": "Orlando is a mesmerizing tale of transformation and identity. Woolf's prose is enchanting, and the exploration of gender and time is thought-provoking.",
#     "short_review": "Mesmerizing tale!"
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "1b1f18d6-05c6-443d-94bf-c42595b16506",
#     "book_rating": 4,
#     "book_review": "The Death of Ivan Ilyich is a profound reflection on life and mortality. Tolstoy's examination of existential themes is both haunting and enlightening.",
#     "short_review": "Profound reflection."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "4bad32a8-6fba-4f3e-bff5-68d675149a9b",
#     "book_rating": 3,
#     "book_review": "Orlando is an interesting blend of fantasy and biography. While the concept is intriguing, I found the execution to be somewhat disjointed.",
#     "short_review": "Interesting blend."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "1b1f18d6-05c6-443d-94bf-c42595b16506",
#     "book_rating": 2,
#     "book_review": "The Death of Ivan Ilyich left me feeling unsatisfied. The protagonist's journey felt shallow, and the narrative lacked depth.",
#     "short_review": "Unsatisfying."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "4bad32a8-6fba-4f3e-bff5-68d675149a9b",
#     "book_rating": 5,
#     "book_review": "Orlando is a masterpiece of modernist literature. Woolf's exploration of gender fluidity and historical narrative is groundbreaking.",
#     "short_review": "Masterpiece!"
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "1b1f18d6-05c6-443d-94bf-c42595b16506",
#     "book_rating": 4,
#     "book_review": "The Death of Ivan Ilyich offers a profound meditation on the nature of life and death. Tolstoy's writing is deeply introspective and emotionally resonant.",
#     "short_review": "Profound meditation."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "4bad32a8-6fba-4f3e-bff5-68d675149a9b",
#     "book_rating": 3,
#     "book_review": "Orlando is an ambitious novel with an interesting premise. However, I found some parts to be tedious and overly descriptive.",
#     "short_review": "Ambitious but tedious."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "1b1f18d6-05c6-443d-94bf-c42595b16506",
#     "book_rating": 5,
#     "book_review": "The Death of Ivan Ilyich is a haunting portrayal of mortality and the human condition. Tolstoy's prose is profound and poignant, leaving a lasting impact.",
#     "short_review": "Haunting portrayal."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "d0abc5bc-8dc2-40a2-8670-a57bd1f0ca74",
#     "book_rating": 5,
#     "book_review": "The Brothers Karamazov is a masterpiece of Russian literature. Dostoevsky's exploration of morality, faith, and family dynamics is profound and thought-provoking.",
#     "short_review": "Masterpiece!"
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "3a9423c9-5500-468d-ad74-871ce83dc158",
#     "book_rating": 4,
#     "book_review": "Notes from Underground is a compelling and introspective work. Dostoevsky's portrayal of the human psyche is both unsettling and captivating.",
#     "short_review": "Compelling read!"
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "d0abc5bc-8dc2-40a2-8670-a57bd1f0ca74",
#     "book_rating": 3,
#     "book_review": "The Brothers Karamazov is a challenging read. While the philosophical themes are intriguing, the narrative can be dense and difficult to follow.",
#     "short_review": "Challenging read."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "3a9423c9-5500-468d-ad74-871ce83dc158",
#     "book_rating": 2,
#     "book_review": "Notes from Underground left me feeling disappointed. The protagonist's ramblings felt tedious and pretentious.",
#     "short_review": "Disappointing."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "d0abc5bc-8dc2-40a2-8670-a57bd1f0ca74",
#     "book_rating": 5,
#     "book_review": "The Brothers Karamazov is a profound exploration of the human condition. Dostoevsky's characters are vividly drawn, and the plot is rich with philosophical depth.",
#     "short_review": "Profound exploration."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "3a9423c9-5500-468d-ad74-871ce83dc158",
#     "book_rating": 4,
#     "book_review": "Notes from Underground is a dark and introspective novel. Dostoevsky's examination of alienation and existential angst is both unsettling and enlightening.",
#     "short_review": "Dark and introspective."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "d0abc5bc-8dc2-40a2-8670-a57bd1f0ca74",
#     "book_rating": 3,
#     "book_review": "The Brothers Karamazov is a classic work, but I found some parts to be overly philosophical and verbose.",
#     "short_review": "Classic but verbose."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "3a9423c9-5500-468d-ad74-871ce83dc158",
#     "book_rating": 5,
#     "book_review": "Notes from Underground is a compelling portrayal of the human psyche. Dostoevsky's insights into the complexities of human nature are unparalleled.",
#     "short_review": "Compelling portrayal."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "63970168-6e81-4cf4-b388-1052bacf712e",
#     "book_rating": 4,
#     "book_review": "For Whom the Bell Tolls is a powerful and evocative novel set during the Spanish Civil War. Hemingway's portrayal of the characters' struggles and the brutality of war is gripping.",
#     "short_review": "Powerful and gripping."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "bf0350e9-25d4-42bb-8c68-ec8f243e1755",
#     "book_rating": 5,
#     "book_review": "A Farewell to Arms is a timeless classic that explores the harsh realities of war and the complexities of love. Hemingway's prose is both beautiful and haunting.",
#     "short_review": "Timeless classic!"
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "63970168-6e81-4cf4-b388-1052bacf712e",
#     "book_rating": 3,
#     "book_review": "For Whom the Bell Tolls has its moments, but I found some parts to be slow-paced. The themes are important, but the execution could have been better.",
#     "short_review": "Has its moments."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "bf0350e9-25d4-42bb-8c68-ec8f243e1755",
#     "book_rating": 2,
#     "book_review": "A Farewell to Arms left me disappointed. The plot felt predictable, and the characters lacked depth.",
#     "short_review": "Disappointing."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "63970168-6e81-4cf4-b388-1052bacf712e",
#     "book_rating": 5,
#     "book_review": "For Whom the Bell Tolls is a masterfully written novel that captures the essence of wartime struggle and sacrifice. Hemingway's prose is both poignant and profound.",
#     "short_review": "Masterfully written."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "bf0350e9-25d4-42bb-8c68-ec8f243e1755",
#     "book_rating": 4,
#     "book_review": "A Farewell to Arms is a compelling narrative that beautifully captures the chaos and heartbreak of war. Hemingway's portrayal of love amidst adversity is deeply moving.",
#     "short_review": "Compelling narrative."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "63970168-6e81-4cf4-b388-1052bacf712e",
#     "book_rating": 3,
#     "book_review": "For Whom the Bell Tolls is an important literary work, but I struggled to connect with the characters. The pacing felt uneven at times.",
#     "short_review": "Important but uneven."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "bf0350e9-25d4-42bb-8c68-ec8f243e1755",
#     "book_rating": 4,
#     "book_review": "A Farewell to Arms is a poignant and heartbreaking tale of love and loss amidst the chaos of war. Hemingway's writing style is both powerful and restrained.",
#     "short_review": "Poignant and heartbreaking."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "af368a43-b2b8-4e26-a947-51b2a7b09696",
#     "book_rating": 5,
#     "book_review": "The Hobbit is an enchanting tale filled with adventure and wonder. Tolkien's world-building is exceptional, and the characters are memorable.",
#     "short_review": "Enchanting tale!"
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "4e73e36a-1496-4566-b39a-016b04a2b6c2",
#     "book_rating": 4,
#     "book_review": "Animal Farm is a thought-provoking allegory that offers insights into politics and human nature. Orwell's writing is concise yet impactful.",
#     "short_review": "Thought-provoking."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "af368a43-b2b8-4e26-a947-51b2a7b09696",
#     "book_rating": 3,
#     "book_review": "The Hobbit was enjoyable, but I found some parts to be slow-paced. Nonetheless, Tolkien's creativity shines through.",
#     "short_review": "Enjoyable but slow-paced."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "4e73e36a-1496-4566-b39a-016b04a2b6c2",
#     "book_rating": 2,
#     "book_review": "Animal Farm disappointed me. While the allegory is clever, I found the execution lacking. The characters felt one-dimensional.",
#     "short_review": "Disappointing execution."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "af368a43-b2b8-4e26-a947-51b2a7b09696",
#     "book_rating": 5,
#     "book_review": "The Hobbit is a timeless classic that appeals to readers of all ages. Tolkien's imagination transports you to a magical world filled with dragons, elves, and dwarves.",
#     "short_review": "Timeless classic!"
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "4e73e36a-1496-4566-b39a-016b04a2b6c2",
#     "book_rating": 4,
#     "book_review": "Animal Farm is a chilling critique of totalitarianism and corrupt leadership. Orwell's allegorical storytelling is both clever and unsettling.",
#     "short_review": "Chilling critique."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "af368a43-b2b8-4e26-a947-51b2a7b09696",
#     "book_rating": 3,
#     "book_review": "The Hobbit is a classic adventure, but I found the pacing uneven at times. Nonetheless, Tolkien's world-building is impressive.",
#     "short_review": "Classic adventure."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "4e73e36a-1496-4566-b39a-016b04a2b6c2",
#     "book_rating": 5,
#     "book_review": "Animal Farm is a brilliant satire that remains relevant today. Orwell's writing is incisive, and the allegory is executed flawlessly.",
#     "short_review": "Brilliant satire!"
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "79e3a677-fb5d-4fd9-80be-ac66ab17196e",
#     "book_rating": 4,
#     "book_review": "The Sound and the Fury is a complex and challenging read, but it rewards those who persevere. Faulkner's writing style may be difficult to follow at times, but the depth of the characters and themes makes it worthwhile.",
#     "short_review": "Complex and rewarding."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "620cdcdc-1f5b-4822-9612-8d82467e9c20",
#     "book_rating": 5,
#     "book_review": "Murder on the Orient Express is a thrilling mystery that keeps you guessing until the end. Agatha Christie's plot twists and intricate characters make it a masterpiece of detective fiction.",
#     "short_review": "Thrilling mystery!"
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "7fcf3d23-419c-454b-850f-1c07317caf8c",
#     "book_rating": 2,
#     "book_review": "Ulysses is an ambitious and experimental novel, but I found it excessively dense and convoluted. Joyce's stream-of-consciousness style made it difficult for me to connect with the story.",
#     "short_review": "Ambitious but dense."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "79e3a677-fb5d-4fd9-80be-ac66ab17196e",
#     "book_rating": 3,
#     "book_review": "The Sound and the Fury is a literary masterpiece with its intricate narrative structure and profound exploration of human consciousness. However, its non-linear storytelling may not be for everyone.",
#     "short_review": "Literary masterpiece."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "620cdcdc-1f5b-4822-9612-8d82467e9c20",
#     "book_rating": 4,
#     "book_review": "Murder on the Orient Express is a classic whodunit that keeps readers engaged from start to finish. Agatha Christie's plot twists are expertly crafted, making it a must-read for mystery enthusiasts.",
#     "short_review": "Engaging whodunit."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "7fcf3d23-419c-454b-850f-1c07317caf8c",
#     "book_rating": 5,
#     "book_review": "Ulysses is a literary tour de force that pushes the boundaries of conventional storytelling. Joyce's innovative use of language and symbolism creates a rich and immersive reading experience.",
#     "short_review": "Innovative storytelling."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "79e3a677-fb5d-4fd9-80be-ac66ab17196e",
#     "book_rating": 3,
#     "book_review": "The Sound and the Fury is a challenging read due to its nonlinear narrative structure, but it offers profound insights into the human condition. Faulkner's writing style is both beautiful and bewildering.",
#     "short_review": "Profound insights."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "620cdcdc-1f5b-4822-9612-8d82467e9c20",
#     "book_rating": 4,
#     "book_review": "Murder on the Orient Express is a captivating mystery with a clever plot and well-developed characters. Agatha Christie's storytelling prowess shines through in this classic novel.",
#     "short_review": "Captivating mystery."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "b837fef5-40fb-474e-ba91-87c717c37544",
#     "book_rating": 4,
#     "book_review": "The Trial is a thought-provoking novel that explores themes of bureaucracy and existentialism. Kafka's writing style is captivating, although the story can be unsettling at times.",
#     "short_review": "Thought-provoking."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "5c6d507d-0b1f-494f-86b2-61f5a64e1fbe",
#     "book_rating": 5,
#     "book_review": "Beloved is a powerful and haunting novel that delves into the legacy of slavery and its impact on individuals and families. Morrison's prose is beautifully crafted, and the story stays with you long after reading.",
#     "short_review": "Powerful and haunting."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "cdd9ff82-fbbe-4473-9469-4e639ec6eaf5",
#     "book_rating": 3,
#     "book_review": "One Hundred Years of Solitude is an ambitious novel with its intricate storytelling and magical realism. While some may find it enchanting, I struggled to connect with the multitude of characters and their interwoven stories.",
#     "short_review": "Ambitious but challenging."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "b837fef5-40fb-474e-ba91-87c717c37544",
#     "book_rating": 4,
#     "book_review": "The Trial is a surreal journey into the absurdity of modern society. Kafka's portrayal of bureaucracy and the individual's struggle against it is both unsettling and thought-provoking.",
#     "short_review": "Surreal and thought-provoking."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "5c6d507d-0b1f-494f-86b2-61f5a64e1fbe",
#     "book_rating": 5,
#     "book_review": "Beloved is a masterful work of literature that confronts the horrors of slavery with raw honesty and empathy. Morrison's storytelling is deeply moving, making this a must-read for all.",
#     "short_review": "Masterful and moving."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "cdd9ff82-fbbe-4473-9469-4e639ec6eaf5",
#     "book_rating": 4,
#     "book_review": "One Hundred Years of Solitude is a mesmerizing tale that spans generations, blending reality with myth and magic. García Márquez's prose is enchanting, although the nonlinear narrative may require patience.",
#     "short_review": "Mesmerizing and enchanting."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "b837fef5-40fb-474e-ba91-87c717c37544",
#     "book_rating": 3,
#     "book_review": "The Trial offers a surreal exploration of the absurdity of the legal system. While Kafka's writing is compelling, the lack of resolution may frustrate some readers.",
#     "short_review": "Surreal exploration."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "5c6d507d-0b1f-494f-86b2-61f5a64e1fbe",
#     "book_rating": 4,
#     "book_review": "Beloved is a haunting and evocative novel that captures the pain and resilience of its characters. Morrison's prose is lyrical, and the story stays with you long after finishing.",
#     "short_review": "Haunting and evocative."
#   },
#     {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "206b9fe4-f7c1-4549-9641-c025ce74cf06",
#     "book_rating": 4,
#     "book_review": "Norwegian Wood is a beautifully written novel that explores themes of love, loss, and coming of age. Murakami's prose is captivating, and the characters are deeply relatable.",
#     "short_review": "Beautifully written."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "d324d5df-fe08-4bf6-9eeb-f1cab73f121b",
#     "book_rating": 5,
#     "book_review": "1Q84 is a masterpiece of storytelling, blending elements of fantasy and mystery seamlessly. Murakami's imagination knows no bounds, and the intricate plot keeps you hooked till the end.",
#     "short_review": "Masterpiece of storytelling."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "805bf29a-9afa-4e20-81ab-92c25868a9e2",
#     "book_rating": 4,
#     "book_review": "Harry Potter and the Chamber of Secrets is a delightful continuation of the wizarding world saga. Rowling's storytelling remains captivating, and the magical world she creates is enchanting.",
#     "short_review": "Delightful continuation."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "206b9fe4-f7c1-4549-9641-c025ce74cf06",
#     "book_rating": 3,
#     "book_review": "Norwegian Wood is a poignant tale of love and loss, but I found the pacing to be a bit slow at times. However, Murakami's introspective narrative style is still engaging.",
#     "short_review": "Poignant but slow pacing."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "d324d5df-fe08-4bf6-9eeb-f1cab73f121b",
#     "book_rating": 5,
#     "book_review": "1Q84 is an enthralling journey into a surreal world where reality and fantasy intertwine. Murakami's ability to blend genres and create complex characters is unparalleled.",
#     "short_review": "Enthralling journey."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "805bf29a-9afa-4e20-81ab-92c25868a9e2",
#     "book_rating": 4,
#     "book_review": "Harry Potter and the Chamber of Secrets is a magical adventure that continues to captivate readers of all ages. Rowling's world-building and character development are exceptional.",
#     "short_review": "Magical adventure."
#   },
#     {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "52767cd1-098b-46f1-9758-c8d6ceda6a69",
#     "book_rating": 5,
#     "book_review": "The Stand is an epic tale of survival and human nature. King's storytelling is masterful, and the characters are richly developed. A must-read for fans of post-apocalyptic fiction.",
#     "short_review": "Masterful storytelling."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "50617fb5-d986-4002-80f5-161bdf1bd29f",
#     "book_rating": 4,
#     "book_review": "And Still I Rise is a powerful collection of poems that inspire resilience and strength. Angelou's words resonate deeply, offering hope and empowerment to all who read them.",
#     "short_review": "Powerful and inspiring."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "fd2d8199-f285-4b4d-95c4-acd2b8c58023",
#     "book_rating": 3,
#     "book_review": "Cat's Cradle is an intriguing and thought-provoking novel that explores the consequences of science and technology. Vonnegut's satire is sharp, but the plot felt disjointed at times.",
#     "short_review": "Intriguing but disjointed."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "50617fb5-d986-4002-80f5-161bdf1bd29f",
#     "book_rating": 5,
#     "book_review": "And Still I Rise is a masterpiece that celebrates the resilience of the human spirit. Angelou's poetry is both empowering and uplifting, inspiring readers to overcome adversity.",
#     "short_review": "Empowering masterpiece."
#   },
#     {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "ea7c29e2-a0ef-4ccd-8c13-13226fe5f9d0",
#     "book_rating": 3,
#     "book_review": "Go Set a Watchman is an intriguing sequel to To Kill a Mockingbird, offering readers a glimpse into the complexities of the characters' lives. While it lacks the impact of its predecessor, it still raises thought-provoking questions about identity and family.",
#     "short_review": "Intriguing sequel."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "ebce05f7-237f-410d-9d75-72b00bb1ca8b",
#     "book_rating": 4,
#     "book_review": "Fahrenheit 451 is a compelling dystopian novel that explores the dangers of censorship and the power of knowledge. Bradbury's writing is both thought-provoking and haunting, leaving a lasting impact on readers.",
#     "short_review": "Compelling and thought-provoking."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "94b08bcf-57a4-440f-9d04-3997e03bdb2e",
#     "book_rating": 2,
#     "book_review": "The War of the Worlds is a classic science fiction novel that has not aged well. While the concept is interesting, the execution feels dated, and the pacing is slow. Overall, it failed to engage me as a reader.",
#     "short_review": "Dated and slow-paced."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "ebce05f7-237f-410d-9d75-72b00bb1ca8b",
#     "book_rating": 5,
#     "book_review": "Fahrenheit 451 is a thought-provoking masterpiece that explores the dangers of censorship and the importance of intellectual freedom. Bradbury's prose is both poetic and powerful, making it a must-read for all lovers of literature.",
#     "short_review": "Poetic masterpiece."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "9b22756c-bebf-4cda-a0aa-8fb22d733681",
#     "book_rating": 4,
#     "book_review": "The Tell-Tale Heart and Other Writings is a captivating collection of Edgar Allan Poe's works. Each story is masterfully crafted, drawing readers into the dark and mysterious world of Poe's imagination.",
#     "short_review": "Captivating collection."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "a8d8dbe3-40ff-4784-a3db-05ad1f550185",
#     "book_rating": 5,
#     "book_review": "Selected Poems of Emily Dickinson is a beautiful anthology showcasing the poet's unique style and profound insights. Dickinson's poetry touches the soul and leaves a lasting impression on readers.",
#     "short_review": "Beautiful anthology."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "4bca2528-955e-4aec-b96a-5f4afc8d8fc3",
#     "book_rating": 3,
#     "book_review": "The Weary Blues is an interesting collection of Langston Hughes' poetry, but it lacks the depth and resonance found in some of his other works. While some poems shine, others feel uninspired.",
#     "short_review": "Mixed feelings."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "a8d8dbe3-40ff-4784-a3db-05ad1f550185",
#     "book_rating": 4,
#     "book_review": "Selected Poems of Emily Dickinson is a thought-provoking collection that showcases the poet's mastery of language and deep understanding of the human condition. Each poem offers a glimpse into the complexities of life and emotion.",
#     "short_review": "Thought-provoking."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "bf0f6e2b-2aa4-4668-a18d-5985bc3ed428",
#     "book_rating": 5,
#     "book_review": "The Collected Poems of Langston Hughes is an extraordinary compilation of his work that beautifully captures the essence of the Harlem Renaissance. Hughes' poetry resonates with timeless themes of identity, struggle, and resilience, making this collection a must-read for poetry enthusiasts.",
#     "short_review": "Extraordinary."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "594a2650-3005-404d-85db-6a2a33040b56",
#     "book_rating": 4,
#     "book_review": "The Bell Jar offers a poignant portrayal of mental illness and societal pressures through the lens of protagonist Esther Greenwood. Sylvia Plath's prose is hauntingly beautiful, drawing readers into Esther's world of despair and introspection.",
#     "short_review": "Poignant."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "bf0f6e2b-2aa4-4668-a18d-5985bc3ed428",
#     "book_rating": 3,
#     "book_review": "While The Collected Poems of Langston Hughes showcases the poet's talent and cultural significance, some of the poems lack the depth and impact found in his more renowned works. Nonetheless, it offers valuable insights into African American history and identity.",
#     "short_review": "Mixed feelings."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "594a2650-3005-404d-85db-6a2a33040b56",
#     "book_rating": 2,
#     "book_review": "While The Bell Jar explores important themes, such as mental illness and societal expectations, Sylvia Plath's writing style can feel overly dramatic and self-indulgent at times. The protagonist's journey lacks nuance and depth, making it difficult to fully engage with the story.",
#     "short_review": "Overly dramatic."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "bf0f6e2b-2aa4-4668-a18d-5985bc3ed428",
#     "book_rating": 4,
#     "book_review": "The Collected Poems of Langston Hughes is a treasure trove of literary gems that celebrate the African American experience with grace and authenticity. Hughes' powerful imagery and poignant storytelling make this collection a timeless classic.",
#     "short_review": "A treasure trove."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "594a2650-3005-404d-85db-6a2a33040b56",
#     "book_rating": 3,
#     "book_review": "The Bell Jar provides a candid exploration of mental illness and the challenges faced by women in the 1950s. While Sylvia Plath's writing is undeniably evocative, the novel's pacing can feel sluggish, and certain passages lack clarity.",
#     "short_review": "Candid exploration."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "316a8af2-1946-44ca-b01d-099130775132",
#     "book_rating": 4,
#     "book_review": "Brave New World is a thought-provoking exploration of a dystopian society where technology and conditioning control every aspect of life. While the novel's themes are compelling, some readers may find its portrayal of human nature and freedom overly pessimistic.",
#     "short_review": "Thought-provoking dystopia."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "316a8af2-1946-44ca-b01d-099130775132",
#     "book_rating": 5,
#     "book_review": "Brave New World is a captivating critique of a society obsessed with consumerism and superficial happiness. Huxley's vision of a world where individuality is sacrificed for stability resonates deeply in today's world, making it a must-read for any lover of dystopian fiction.",
#     "short_review": "Captivating critique."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "316a8af2-1946-44ca-b01d-099130775132",
#     "book_rating": 3,
#     "book_review": "While Brave New World presents a chilling vision of a future society controlled by technology and conditioning, some aspects of the novel feel dated and overly didactic. However, Huxley's exploration of themes such as individuality and conformity still holds relevance today.",
#     "short_review": "Chilling vision."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "aea16536-842b-4108-9d5a-bb0cb5bb8704",
#     "book_rating": 5,
#     "book_review": "Moby-Dick is an epic tale that explores the depths of human obsession and the vastness of the sea. Melville's prose is rich and immersive, drawing readers into the world of whaling ships and larger-than-life characters. A must-read for anyone who loves adventure and literary depth.",
#     "short_review": "Epic adventure."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "aea16536-842b-4108-9d5a-bb0cb5bb8704",
#     "book_rating": 4,
#     "book_review": "Moby-Dick is a towering achievement in American literature, blending adventure, philosophy, and seafaring lore into a gripping narrative. While some may find Melville's digressions and dense prose challenging, the novel's exploration of themes such as fate and revenge make it a rewarding read.",
#     "short_review": "Towering achievement."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "aea16536-842b-4108-9d5a-bb0cb5bb8704",
#     "book_rating": 3,
#     "book_review": "Moby-Dick is a classic work that delves into the complexities of human nature and the relentless pursuit of a goal. While Melville's prose can be dense and verbose at times, the novel's themes of obsession and fate still resonate with readers today.",
#     "short_review": "Complex exploration."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "798b9ad0-6893-4a78-aaeb-4f979fd69784",
#     "book_rating": 5,
#     "book_review": "Little Women is a heartwarming tale of sisterhood, love, and resilience. Louisa May Alcott beautifully captures the joys and struggles of growing up, making this classic novel a timeless favorite for readers of all ages.",
#     "short_review": "Heartwarming tale."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "798b9ad0-6893-4a78-aaeb-4f979fd69784",
#     "book_rating": 4,
#     "book_review": "Little Women is a delightful story that celebrates the bonds of family and the pursuit of dreams. Alcott's characters are relatable and endearing, and her writing style is engaging throughout.",
#     "short_review": "Delightful story."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "798b9ad0-6893-4a78-aaeb-4f979fd69784",
#     "book_rating": 3,
#     "book_review": "While Little Women is a classic novel with memorable characters and timeless themes, some readers may find its pacing slow and its moral lessons heavy-handed. However, its exploration of sisterhood and female empowerment remains relevant today.",
#     "short_review": "Memorable characters."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "b798c783-331d-461a-b71d-e1a9ae039408",
#     "book_rating": 5,
#     "book_review": "The Picture of Dorian Gray is a gripping tale of vanity, decadence, and the consequences of unchecked ambition. Oscar Wilde's wit and satire shine through in this haunting exploration of morality and the pursuit of beauty.",
#     "short_review": "Gripping tale."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "b798c783-331d-461a-b71d-e1a9ae039408",
#     "book_rating": 4,
#     "book_review": "The Picture of Dorian Gray is a mesmerizing novel that delves into the depths of human desire and the allure of eternal youth. Wilde's prose is both elegant and provocative, making this a captivating read from start to finish.",
#     "short_review": "Mesmerizing novel."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "b798c783-331d-461a-b71d-e1a9ae039408",
#     "book_rating": 3,
#     "book_review": "While The Picture of Dorian Gray offers a fascinating exploration of aestheticism and morality, some readers may find Wilde's philosophical digressions tedious. However, the novel's central premise and vivid imagery make it worth the read.",
#     "short_review": "Fascinating exploration."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "69ce7a43-47fc-410a-8f95-9a16c94b1a87",
#     "book_rating": 5,
#     "book_review": "The Importance of Being Earnest is a delightful comedy filled with wit and humor. Oscar Wilde's sharp dialogue and clever wordplay make it a timeless classic that is sure to entertain readers of all ages.",
#     "short_review": "Delightful comedy."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "69ce7a43-47fc-410a-8f95-9a16c94b1a87",
#     "book_rating": 4,
#     "book_review": "The Importance of Being Earnest is a brilliant satire that offers a scathing critique of Victorian society. Wilde's clever observations and witty repartee make it a must-read for fans of classic literature.",
#     "short_review": "Brilliant satire."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "69ce7a43-47fc-410a-8f95-9a16c94b1a87",
#     "book_rating": 3,
#     "book_review": "While The Importance of Being Earnest is undeniably witty and entertaining, some readers may find its humor and social commentary dated. However, its timeless themes of love, identity, and societal expectations still resonate today.",
#     "short_review": "Undeniably witty."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "ca9e6acc-42f6-4d2c-991c-0741e64667c4",
#     "book_rating": 5,
#     "book_review": "The Adventures of Sherlock Holmes is a captivating collection of detective stories that showcases Arthur Conan Doyle's masterful storytelling and keen attention to detail. Each mystery is cleverly crafted, keeping readers on the edge of their seats until the very end.",
#     "short_review": "Captivating collection."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "ca9e6acc-42f6-4d2c-991c-0741e64667c4",
#     "book_rating": 4,
#     "book_review": "The Adventures of Sherlock Holmes is a classic work of detective fiction that has stood the test of time. Doyle's iconic character, Sherlock Holmes, is brilliantly portrayed, and each story is intricately plotted, making it a must-read for mystery enthusiasts.",
#     "short_review": "Classic detective fiction."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "ca9e6acc-42f6-4d2c-991c-0741e64667c4",
#     "book_rating": 3,
#     "book_review": "While The Adventures of Sherlock Holmes is undeniably clever and engaging, some readers may find its formulaic structure predictable. However, the charm of Sherlock Holmes and the intrigue of the mysteries still make it a worthwhile read.",
#     "short_review": "Engaging mysteries."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "724047b5-8329-412c-bd73-c3d6c7dc4b5d",
#     "book_rating": 5,
#     "book_review": "The Grapes of Wrath is a powerful and poignant novel that vividly captures the struggles of the Great Depression era. Steinbeck's evocative prose and compelling characters make it a hauntingly beautiful depiction of the human spirit in the face of adversity.",
#     "short_review": "Powerful and poignant."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "724047b5-8329-412c-bd73-c3d6c7dc4b5d",
#     "book_rating": 4,
#     "book_review": "The Grapes of Wrath is a classic American novel that offers a profound exploration of social injustice and the plight of the working class. Steinbeck's vivid descriptions and compelling narrative make it a thought-provoking read.",
#     "short_review": "Profound exploration."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "724047b5-8329-412c-bd73-c3d6c7dc4b5d",
#     "book_rating": 3,
#     "book_review": "While The Grapes of Wrath is undeniably well-written and thought-provoking, some readers may find its pacing slow and its social commentary heavy-handed. However, its themes of resilience and solidarity are still relevant today.",
#     "short_review": "Well-written and thought-provoking."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "99dbba88-cf20-4722-869a-887a66ac5f9a",
#     "book_rating": 4,
#     "book_review": "The Great Gatsby is a captivating novel that beautifully captures the glamour and decadence of the Jazz Age. F. Scott Fitzgerald's prose is both elegant and evocative, transporting readers to a bygone era.",
#     "short_review": "Captivating novel."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "99dbba88-cf20-4722-869a-887a66ac5f9a",
#     "book_rating": 5,
#     "book_review": "The Great Gatsby is a timeless classic that explores themes of love, wealth, and the American Dream. Fitzgerald's vivid characters and lyrical prose make it a must-read for literature enthusiasts.",
#     "short_review": "Timeless classic."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "99dbba88-cf20-4722-869a-887a66ac5f9a",
#     "book_rating": 3,
#     "book_review": "While The Great Gatsby is undeniably well-written and atmospheric, some readers may find its characters and themes shallow. However, its depiction of the Roaring Twenties is still relevant today.",
#     "short_review": "Well-written and atmospheric."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "99dbba88-cf20-4722-869a-887a66ac5f9a",
#     "book_rating": 2,
#     "book_review": "The Great Gatsby is a disappointing read that fails to live up to its hype. While the prose is elegant, the characters are unlikable and the plot is shallow.",
#     "short_review": "Disappointing read."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "90f4c594-fc80-45d3-8948-8687afe57299",
#     "book_rating": 5,
#     "book_review": "American Gods is a mesmerizing blend of mythology, fantasy, and Americana. Neil Gaiman's imagination knows no bounds, and his vivid storytelling makes this book an unforgettable journey.",
#     "short_review": "Mesmerizing blend."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "90f4c594-fc80-45d3-8948-8687afe57299",
#     "book_rating": 4,
#     "book_review": "American Gods is a unique and captivating novel that explores the nature of belief and the power of myth. Gaiman's prose is both lyrical and thought-provoking, making it a must-read for fans of fantasy.",
#     "short_review": "Unique and captivating."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "90f4c594-fc80-45d3-8948-8687afe57299",
#     "book_rating": 3,
#     "book_review": "While American Gods is undeniably ambitious and imaginative, some readers may find its pacing slow and its plot convoluted. However, its rich mythology and complex characters make it a rewarding read for those who persevere.",
#     "short_review": "Ambitious and imaginative."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "7c5443be-10b1-4f70-a30f-58382b6971b0",
#     "book_rating": 4,
#     "book_review": "Do Androids Dream of Electric Sheep? is a thought-provoking science fiction novel that raises important questions about identity, empathy, and the nature of humanity. Philip K. Dick's vision of a dystopian future is both chilling and compelling.",
#     "short_review": "Thought-provoking science fiction."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "7c5443be-10b1-4f70-a30f-58382b6971b0",
#     "book_rating": 3,
#     "book_review": "Do Androids Dream of Electric Sheep? is a fascinating exploration of artificial intelligence and what it means to be human. While the pacing can be slow at times, Dick's philosophical insights make it a worthwhile read.",
#     "short_review": "Fascinating exploration."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "7c5443be-10b1-4f70-a30f-58382b6971b0",
#     "book_rating": 5,
#     "book_review": "Do Androids Dream of Electric Sheep? is a masterpiece of science fiction that remains relevant in today's world of advancing technology. Dick's exploration of the blurred lines between man and machine is both thought-provoking and deeply moving.",
#     "short_review": "Masterpiece of science fiction."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "a2d912c2-257e-4028-a0ec-9bda804742e5",
#     "book_rating": 4,
#     "book_review": "The Man in the High Castle is a thought-provoking alternative history novel that explores the consequences of a world where the Axis powers won World War II. Philip K. Dick's imaginative storytelling and attention to detail make it a compelling read.",
#     "short_review": "Thought-provoking alternative history."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "a2d912c2-257e-4028-a0ec-9bda804742e5",
#     "book_rating": 5,
#     "book_review": "The Man in the High Castle is a masterpiece of speculative fiction that offers a chilling glimpse into a world where the Nazis and Japanese have divided America. Dick's exploration of identity and reality is both profound and unsettling.",
#     "short_review": "Masterpiece of speculative fiction."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "a2d912c2-257e-4028-a0ec-9bda804742e5",
#     "book_rating": 3,
#     "book_review": "While The Man in the High Castle presents an intriguing premise, some readers may find its pacing uneven and its plot convoluted. However, its exploration of alternate history and moral ambiguity still makes it a worthwhile read.",
#     "short_review": "Intriguing premise."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "a2d912c2-257e-4028-a0ec-9bda804742e5",
#     "book_rating": 2,
#     "book_review": "The Man in the High Castle is a disappointing novel that fails to deliver on its intriguing premise. The narrative lacks coherence, and the characters feel underdeveloped.",
#     "short_review": "Disappointing read."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "eb9a566a-7020-4ef8-b168-3d68aa39d23c",
#     "book_rating": 5,
#     "book_review": "The Handmaid's Tale is a chilling dystopian novel that offers a stark warning about the dangers of totalitarianism and the erosion of women's rights. Margaret Atwood's prose is both lyrical and haunting, making it a powerful and unforgettable read.",
#     "short_review": "Chilling dystopian novel."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "eb9a566a-7020-4ef8-b168-3d68aa39d23c",
#     "book_rating": 4,
#     "book_review": "The Handmaid's Tale is a provocative and timely novel that explores issues of power, control, and gender oppression. Atwood's stark portrayal of a dystopian society is both unsettling and thought-provoking.",
#     "short_review": "Provocative and timely."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "eb9a566a-7020-4ef8-b168-3d68aa39d23c",
#     "book_rating": 3,
#     "book_review": "While The Handmaid's Tale is undeniably well-written and thought-provoking, some readers may find its pacing slow and its narrative structure disjointed. However, its themes of oppression and resistance are still relevant today.",
#     "short_review": "Well-written but slow pacing."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "cb537a82-c01f-47ec-b4f4-6437c2134f93",
#     "book_rating": 4,
#     "book_review": "Oryx and Crake is a compelling and thought-provoking dystopian novel that explores the consequences of genetic engineering and corporate greed. Margaret Atwood's vivid imagination and dark humor make it a must-read for fans of speculative fiction.",
#     "short_review": "Compelling and thought-provoking."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "cb537a82-c01f-47ec-b4f4-6437c2134f93",
#     "book_rating": 3,
#     "book_review": "Oryx and Crake presents an intriguing vision of a future ravaged by scientific experimentation and environmental collapse. Atwood's prose is vivid, but the novel's bleak outlook may be too dark for some readers.",
#     "short_review": "Intriguing vision."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "cb537a82-c01f-47ec-b4f4-6437c2134f93",
#     "book_rating": 5,
#     "book_review": "Oryx and Crake is a haunting and unforgettable exploration of humanity's destructive tendencies and the consequences of unchecked scientific progress. Atwood's writing is both beautiful and chilling, making it a standout in the dystopian genre.",
#     "short_review": "Haunting and unforgettable."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "5240bed8-6928-4cec-954e-9461038dc774",
#     "book_rating": 4,
#     "book_review": "My Name Is Red is a captivating novel that immerses readers in the vibrant world of Ottoman Istanbul. Orhan Pamuk's intricate storytelling and rich descriptions make it a truly memorable read.",
#     "short_review": "Captivating historical novel."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "5240bed8-6928-4cec-954e-9461038dc774",
#     "book_rating": 5,
#     "book_review": "My Name Is Red is a masterpiece of storytelling that skillfully blends history, mystery, and art. Pamuk's prose is elegant and evocative, transporting readers to a bygone era.",
#     "short_review": "Masterpiece of storytelling."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "5240bed8-6928-4cec-954e-9461038dc774",
#     "book_rating": 3,
#     "book_review": "While My Name Is Red offers a fascinating glimpse into Ottoman culture and art, some readers may find its pacing slow and its plot overly complex. However, its exploration of love and betrayal still makes it worth reading.",
#     "short_review": "Fascinating but slow-paced."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "5240bed8-6928-4cec-954e-9461038dc774",
#     "book_rating": 2,
#     "book_review": "My Name Is Red is a disappointing novel that fails to live up to its intriguing premise. The narrative is disjointed, and the characters lack depth, making it a struggle to stay engaged.",
#     "short_review": "Disappointing read."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "ef0dd284-1dec-470c-86e4-efa6673688f8",
#     "book_rating": 5,
#     "book_review": "The House of the Spirits is a mesmerizing family saga that spans generations and blends magical realism with political upheaval. Isabel Allende's lush prose and vivid characters make it a literary masterpiece.",
#     "short_review": "Mesmerizing family saga."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "ef0dd284-1dec-470c-86e4-efa6673688f8",
#     "book_rating": 4,
#     "book_review": "The House of the Spirits is an enchanting novel that explores themes of love, power, and destiny against the backdrop of political turmoil. Allende's lyrical prose and vivid imagery create a world that lingers in the imagination.",
#     "short_review": "Enchanting exploration of love and destiny."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "ef0dd284-1dec-470c-86e4-efa6673688f8",
#     "book_rating": 3,
#     "book_review": "While The House of the Spirits boasts lush prose and an ambitious narrative, some readers may find its length daunting and its plot meandering. However, its exploration of familial bonds and societal change is still compelling.",
#     "short_review": "Lush prose but meandering plot."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "b8a5caad-d6d7-4f3d-9522-bfcfe0a5f049",
#     "book_rating": 4,
#     "book_review": "Never Let Me Go is a haunting and thought-provoking novel that explores the ethics of cloning and the nature of humanity. Kazuo Ishiguro's subtle storytelling and nuanced characters leave a lasting impact on readers.",
#     "short_review": "Haunting exploration of ethics."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "b8a5caad-d6d7-4f3d-9522-bfcfe0a5f049",
#     "book_rating": 3,
#     "book_review": "Never Let Me Go presents a compelling premise and raises important ethical questions, but some readers may find its melancholic tone overwhelming. However, its exploration of love and loss is undeniably moving.",
#     "short_review": "Compelling premise but melancholic tone."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "b8a5caad-d6d7-4f3d-9522-bfcfe0a5f049",
#     "book_rating": 5,
#     "book_review": "Never Let Me Go is a beautiful and haunting novel that delves into the human condition and the fragility of life. Ishiguro's prose is luminous, and his exploration of memory and identity is deeply affecting.",
#     "short_review": "Beautiful and haunting."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "495f4da7-6dda-47c9-b012-8df9fc7538c7",
#     "book_rating": 4,
#     "book_review": "The Golden Notebook is a powerful and thought-provoking novel that delves into the complexities of identity and relationships. Doris Lessing's writing is both intimate and insightful, making it a compelling read.",
#     "short_review": "Powerful and thought-provoking."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "495f4da7-6dda-47c9-b012-8df9fc7538c7",
#     "book_rating": 5,
#     "book_review": "The Golden Notebook is a literary masterpiece that boldly explores themes of feminism, politics, and mental health. Lessing's narrative structure is innovative, and her characters are deeply human and relatable.",
#     "short_review": "Literary masterpiece."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "495f4da7-6dda-47c9-b012-8df9fc7538c7",
#     "book_rating": 3,
#     "book_review": "While The Golden Notebook offers a unique perspective on gender and society, some readers may find its nonlinear narrative confusing. However, its exploration of female identity is still relevant and compelling.",
#     "short_review": "Unique perspective but confusing."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "495f4da7-6dda-47c9-b012-8df9fc7538c7",
#     "book_rating": 2,
#     "book_review": "The Golden Notebook is a disappointing read with flat characters and a disjointed plot. Lessing's attempt to tackle multiple themes results in a messy narrative that fails to engage.",
#     "short_review": "Disappointing and messy."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "9c9b218a-a058-487c-8377-f95871c61f44",
#     "book_rating": 5,
#     "book_review": "Lolita is a beautifully written but disturbing novel that challenges readers with its provocative subject matter. Vladimir Nabokov's prose is exquisite, and his exploration of obsession and morality is masterful.",
#     "short_review": "Beautiful but disturbing."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "9c9b218a-a058-487c-8377-f95871c61f44",
#     "book_rating": 4,
#     "book_review": "Lolita is a controversial yet captivating novel that showcases Nabokov's unparalleled literary talent. The story's unreliable narrator adds depth to its exploration of taboo subjects, making it a compelling read.",
#     "short_review": "Controversial yet captivating."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "9c9b218a-a058-487c-8377-f95871c61f44",
#     "book_rating": 3,
#     "book_review": "While Lolita is undeniably well-written, some readers may find its subject matter deeply unsettling. Nabokov's lyrical prose cannot fully overshadow the discomfort caused by the novel's themes.",
#     "short_review": "Well-written but unsettling."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "c1eeea5b-12a6-4044-a2db-88171076226a",
#     "book_rating": 4,
#     "book_review": "Midnight's Children is a sprawling and ambitious novel that masterfully blends history with magical realism. Salman Rushdie's vivid imagery and lyrical prose create a vivid tapestry of postcolonial India.",
#     "short_review": "Sprawling and ambitious."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "c1eeea5b-12a6-4044-a2db-88171076226a",
#     "book_rating": 3,
#     "book_review": "Midnight's Children is an impressive literary feat, but its dense prose and convoluted narrative may be challenging for some readers to navigate. Rushdie's exploration of India's history is nonetheless compelling.",
#     "short_review": "Impressive but challenging."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "c1eeea5b-12a6-4044-a2db-88171076226a",
#     "book_rating": 5,
#     "book_review": "Midnight's Children is a masterpiece that captures the tumultuous history of India with grace and imagination. Rushdie's narrative prowess and rich symbolism make it a must-read for fans of postcolonial literature.",
#     "short_review": "Masterpiece of postcolonial literature."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "c2188b1f-b9be-492f-9b9c-556ab44342b5",
#     "book_rating": 4,
#     "book_review": "The Road is a haunting and powerful post-apocalyptic novel that explores the depths of human resilience and the bond between father and son. Cormac McCarthy's spare prose style adds to the atmosphere of despair and hope.",
#     "short_review": "Haunting and powerful."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "c2188b1f-b9be-492f-9b9c-556ab44342b5",
#     "book_rating": 5,
#     "book_review": "The Road is a masterpiece that evokes a sense of existential dread while also celebrating the human spirit. McCarthy's prose is poetic and visceral, painting a vivid portrait of a desolate world.",
#     "short_review": "Masterpiece of existential dread."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "c2188b1f-b9be-492f-9b9c-556ab44342b5",
#     "book_rating": 3,
#     "book_review": "While The Road offers a bleak and thought-provoking glimpse into a post-apocalyptic future, some readers may find its narrative too bleak and its themes too heavy-handed. However, McCarthy's prose is undeniably powerful.",
#     "short_review": "Bleak but thought-provoking."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "c2188b1f-b9be-492f-9b9c-556ab44342b5",
#     "book_rating": 2,
#     "book_review": "The Road is a tedious and overrated novel that fails to deliver on its promise of profundity. McCarthy's sparse prose style becomes monotonous, and the story lacks depth and character development.",
#     "short_review": "Tedious and overrated."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "8811f52e-6e18-424d-95d9-954cebd53302",
#     "book_rating": 5,
#     "book_review": "The Catcher in the Rye is a timeless coming-of-age novel that resonates with readers of all ages. J.D. Salinger's portrayal of teenage angst and alienation is both poignant and relatable, making it a classic.",
#     "short_review": "Timeless coming-of-age classic."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "8811f52e-6e18-424d-95d9-954cebd53302",
#     "book_rating": 4,
#     "book_review": "The Catcher in the Rye captures the disillusionment and rebellion of youth with honesty and authenticity. Holden Caulfield's voice is distinct and unforgettable, making this novel a must-read for teenagers and adults alike.",
#     "short_review": "Unforgettable voice of youth."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "8811f52e-6e18-424d-95d9-954cebd53302",
#     "book_rating": 3,
#     "book_review": "While The Catcher in the Rye offers an insightful portrayal of adolescent angst, some readers may find Holden Caulfield's cynicism grating. Salinger's narrative style can be repetitive, but the novel still has its moments.",
#     "short_review": "Insightful but repetitive."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "bc5b3eba-b5a3-4f30-b133-37791b5b0ef4",
#     "book_rating": 4,
#     "book_review": "The Color Purple is a powerful and deeply moving novel that explores themes of race, gender, and identity. Alice Walker's prose is lyrical and evocative, and her characters are unforgettable.",
#     "short_review": "Powerful and deeply moving."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "bc5b3eba-b5a3-4f30-b133-37791b5b0ef4",
#     "book_rating": 3,
#     "book_review": "While The Color Purple tackles important issues with sensitivity and insight, some readers may find its narrative structure confusing. Nonetheless, Alice Walker's storytelling is powerful and emotionally resonant.",
#     "short_review": "Sensitive but confusing."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "bc5b3eba-b5a3-4f30-b133-37791b5b0ef4",
#     "book_rating": 5,
#     "book_review": "The Color Purple is a triumph of literature, tackling difficult themes with grace and humanity. Walker's characters are richly drawn, and her prose is both lyrical and powerful. A must-read for anyone interested in social justice.",
#     "short_review": "Triumph of literature."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "4de2c275-4077-49d9-9f68-c92621294160",
#     "book_rating": 4,
#     "book_review": "Things Fall Apart is a poignant portrayal of the clash between traditional African culture and colonialism. Chinua Achebe's vivid descriptions and compelling characters make this a must-read for anyone interested in African literature.",
#     "short_review": "Poignant portrayal."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "4de2c275-4077-49d9-9f68-c92621294160",
#     "book_rating": 5,
#     "book_review": "Things Fall Apart is a powerful novel that delves into the complexities of Nigerian society before and after colonization. Achebe's storytelling is masterful, and the themes of identity and cultural change resonate deeply.",
#     "short_review": "Powerful storytelling."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "4de2c275-4077-49d9-9f68-c92621294160",
#     "book_rating": 3,
#     "book_review": "While Things Fall Apart offers valuable insights into Nigerian culture and history, some readers may find the pacing slow and the prose dense. However, Achebe's exploration of colonialism and its impact remains relevant.",
#     "short_review": "Valuable insights."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "4de2c275-4077-49d9-9f68-c92621294160",
#     "book_rating": 2,
#     "book_review": "Things Fall Apart failed to engage me as a reader. The narrative felt disjointed, and the characters lacked depth. While the themes are important, I found the execution lacking.",
#     "short_review": "Failed to engage."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "e776150b-cd36-4c0f-8178-079bbd3c6622",
#     "book_rating": 5,
#     "book_review": "The Diary of a Young Girl is a harrowing account of Anne Frank's experiences during the Holocaust. Her courage and resilience in the face of unimaginable adversity are inspiring. Every page is imbued with hope and humanity.",
#     "short_review": "Harrowing and inspiring."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "e776150b-cd36-4c0f-8178-079bbd3c6622",
#     "book_rating": 4,
#     "book_review": "The Diary of a Young Girl offers a unique perspective on the Holocaust through the eyes of a young girl. Anne Frank's diary is both heartbreaking and hopeful, reminding us of the power of resilience and the human spirit.",
#     "short_review": "Heartbreaking and hopeful."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "e776150b-cd36-4c0f-8178-079bbd3c6622",
#     "book_rating": 3,
#     "book_review": "While The Diary of a Young Girl provides valuable insights into the Holocaust, some readers may find Anne Frank's writing style repetitive. Nonetheless, her story remains a poignant reminder of the horrors of war.",
#     "short_review": "Valuable insights."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "82411803-f697-4503-bce7-7636bd3a6acc",
#     "book_rating": 4,
#     "book_review": "Jane Eyre is a timeless classic that explores themes of love, independence, and social class. Charlotte Brontë's vivid characters and rich prose make this a captivating read for lovers of Victorian literature.",
#     "short_review": "Timeless classic."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "82411803-f697-4503-bce7-7636bd3a6acc",
#     "book_rating": 3,
#     "book_review": "While Jane Eyre is a well-written novel with complex characters, some readers may find the pacing slow, especially in the early chapters. However, Brontë's exploration of social issues is still relevant today.",
#     "short_review": "Well-written but slow pacing."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "82411803-f697-4503-bce7-7636bd3a6acc",
#     "book_rating": 5,
#     "book_review": "Jane Eyre is a masterpiece of English literature, blending romance, mystery, and social commentary seamlessly. Brontë's portrayal of Jane's inner strength and resilience continues to captivate readers of all ages.",
#     "short_review": "Masterpiece of English literature."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "93cf0e9c-5936-4a98-8500-0840bb7b7740",
#     "book_rating": 4,
#     "book_review": "Frankenstein is a gripping tale of science, ambition, and morality. Mary Shelley's exploration of the consequences of playing god is as relevant today as it was when the novel was first published.",
#     "short_review": "Gripping tale."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "93cf0e9c-5936-4a98-8500-0840bb7b7740",
#     "book_rating": 5,
#     "book_review": "Frankenstein is a masterpiece of Gothic literature that delves into themes of ambition, isolation, and the nature of humanity. Mary Shelley's prose is both haunting and beautiful, making this a timeless classic.",
#     "short_review": "Timeless classic."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "93cf0e9c-5936-4a98-8500-0840bb7b7740",
#     "book_rating": 3,
#     "book_review": "While Frankenstein is undeniably a classic, some readers may find the pacing slow, especially in the middle sections. However, the novel's exploration of scientific ethics remains thought-provoking.",
#     "short_review": "Classic but slow pacing."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "93cf0e9c-5936-4a98-8500-0840bb7b7740",
#     "book_rating": 2,
#     "book_review": "Frankenstein failed to captivate me as a reader. The narrative felt disjointed, and the characters lacked depth. While the premise is intriguing, the execution fell short of my expectations.",
#     "short_review": "Failed to captivate."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "dd6a3890-d32a-40ee-ba83-4eab184ee48a",
#     "book_rating": 5,
#     "book_review": "The Count of Monte Cristo is an epic tale of revenge, betrayal, and redemption. Alexandre Dumas's intricate plot and vivid characters kept me on the edge of my seat from beginning to end. A true masterpiece.",
#     "short_review": "Epic tale."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "dd6a3890-d32a-40ee-ba83-4eab184ee48a",
#     "book_rating": 4,
#     "book_review": "The Count of Monte Cristo is a riveting adventure that explores themes of justice and forgiveness. While the story is lengthy, every twist and turn is worth the journey. Dumas's storytelling prowess shines in this classic.",
#     "short_review": "Riveting adventure."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "dd6a3890-d32a-40ee-ba83-4eab184ee48a",
#     "book_rating": 3,
#     "book_review": "While The Count of Monte Cristo is an engaging tale, some readers may find the plot convoluted and the pacing uneven. However, the novel's exploration of revenge and forgiveness is thought-provoking.",
#     "short_review": "Engaging but convoluted."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "fdce9426-a4f5-4eca-bc9e-6577c007017d",
#     "book_rating": 4,
#     "book_review": "A Tale of Two Cities is a compelling historical novel set against the backdrop of the French Revolution. Charles Dickens's vivid descriptions and memorable characters make this a must-read for fans of classic literature.",
#     "short_review": "Compelling historical novel."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "fdce9426-a4f5-4eca-bc9e-6577c007017d",
#     "book_rating": 3,
#     "book_review": "While A Tale of Two Cities offers a fascinating glimpse into the French Revolution, some readers may find Dickens's writing style verbose and the plot overly melodramatic. Nonetheless, the novel's themes of sacrifice and redemption are timeless.",
#     "short_review": "Fascinating but verbose."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "fdce9426-a4f5-4eca-bc9e-6577c007017d",
#     "book_rating": 5,
#     "book_review": "A Tale of Two Cities is a literary masterpiece that captures the tumultuous spirit of the French Revolution. Dickens's rich storytelling and poignant themes of sacrifice and resurrection make this a timeless classic.",
#     "short_review": "Literary masterpiece."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "2afe9fc2-d209-46a4-a4fb-f77d808368e4",
#     "book_rating": 4,
#     "book_review": "The Jungle Book is a classic collection of stories that vividly brings the jungle to life. Rudyard Kipling's imaginative tales captivate readers of all ages with their adventure and charm.",
#     "short_review": "Captivating tales."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "2afe9fc2-d209-46a4-a4fb-f77d808368e4",
#     "book_rating": 5,
#     "book_review": "The Jungle Book is a timeless masterpiece that transports readers into the heart of the jungle. Kipling's rich descriptions and memorable characters make this a must-read for anyone who loves adventure.",
#     "short_review": "Timeless masterpiece."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "2afe9fc2-d209-46a4-a4fb-f77d808368e4",
#     "book_rating": 3,
#     "book_review": "While The Jungle Book is a classic work of literature, some readers may find the language and themes outdated. However, Kipling's storytelling still holds a certain charm that can appeal to those interested in adventure.",
#     "short_review": "Outdated themes."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "2afe9fc2-d209-46a4-a4fb-f77d808368e4",
#     "book_rating": 2,
#     "book_review": "The Jungle Book failed to capture my interest. The stories felt disjointed, and the characters lacked depth. While it may have been groundbreaking in its time, it does not resonate with modern readers.",
#     "short_review": "Lacked depth."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "80c39dff-06b6-489d-8169-bb58b0ba1f8c",
#     "book_rating": 5,
#     "book_review": "Madame Bovary is a powerful exploration of desire, betrayal, and societal expectations. Gustave Flaubert's prose is exquisite, painting a vivid portrait of Emma Bovary's tragic life.",
#     "short_review": "Powerful exploration."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "80c39dff-06b6-489d-8169-bb58b0ba1f8c",
#     "book_rating": 4,
#     "book_review": "Madame Bovary offers a compelling glimpse into the complexities of human nature. Flaubert's attention to detail and character development make this a timeless classic that continues to resonate with readers.",
#     "short_review": "Compelling glimpse."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "80c39dff-06b6-489d-8169-bb58b0ba1f8c",
#     "book_rating": 3,
#     "book_review": "While Madame Bovary is undeniably well-written, I found the protagonist's actions frustrating and the plot slow-paced. However, Flaubert's exploration of societal norms and gender roles is thought-provoking.",
#     "short_review": "Frustrating protagonist."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "2ddb6885-f7de-4302-a0a7-e949d39f3204",
#     "book_rating": 4,
#     "book_review": "The Scarlet Letter is a classic novel that delves into themes of sin, guilt, and redemption. Nathaniel Hawthorne's prose is elegant and evocative, making this a compelling read from start to finish.",
#     "short_review": "Compelling read."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "2ddb6885-f7de-4302-a0a7-e949d39f3204",
#     "book_rating": 3,
#     "book_review": "The Scarlet Letter is a thought-provoking novel that explores the consequences of societal judgment and hypocrisy. While Hawthorne's writing style may be dense for some, the themes remain relevant to contemporary society.",
#     "short_review": "Thought-provoking."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "2ddb6885-f7de-4302-a0a7-e949d39f3204",
#     "book_rating": 5,
#     "book_review": "The Scarlet Letter is a timeless masterpiece that continues to resonate with readers today. Hawthorne's exploration of sin and redemption is profound, and the novel's themes are as relevant now as they were in the 19th century.",
#     "short_review": "Timeless masterpiece."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "5fc4c664-a78e-45d8-964a-530ce1c97049",
#     "book_rating": 4,
#     "book_review": "Middlemarch is a rich and complex novel that delves deep into the lives of its characters. George Eliot's insightful commentary on society and human nature makes this a rewarding read.",
#     "short_review": "Rich and complex."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "5fc4c664-a78e-45d8-964a-530ce1c97049",
#     "book_rating": 5,
#     "book_review": "Middlemarch is a masterpiece of Victorian literature. Eliot's vivid portrayal of provincial life and her nuanced characters make this novel a timeless classic.",
#     "short_review": "Timeless classic."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "5fc4c664-a78e-45d8-964a-530ce1c97049",
#     "book_rating": 3,
#     "book_review": "While Middlemarch is undoubtedly a well-crafted novel, its length and dense prose may deter some readers. However, those who persevere will find a rewarding exploration of human relationships.",
#     "short_review": "Dense prose."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "5fc4c664-a78e-45d8-964a-530ce1c97049",
#     "book_rating": 2,
#     "book_review": "Middlemarch was a disappointing read for me. The slow pace and multitude of characters made it difficult to engage with the story. While some may appreciate its depth, I found it tedious.",
#     "short_review": "Disappointing read."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "ed7998de-e7d2-4c18-a659-174820e7d9b1",
#     "book_rating": 5,
#     "book_review": "A Doll's House is a groundbreaking play that challenges societal norms and expectations. Henrik Ibsen's exploration of gender roles and identity is as relevant today as it was when the play was first performed.",
#     "short_review": "Groundbreaking play."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "ed7998de-e7d2-4c18-a659-174820e7d9b1",
#     "book_rating": 4,
#     "book_review": "A Doll's House is a thought-provoking play that raises important questions about marriage and individual freedom. Ibsen's skillful storytelling and memorable characters make this a must-read for anyone interested in social issues.",
#     "short_review": "Thought-provoking."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "ed7998de-e7d2-4c18-a659-174820e7d9b1",
#     "book_rating": 3,
#     "book_review": "While A Doll's House addresses significant themes, I found the characters and dialogue somewhat melodramatic. However, I appreciate its historical importance and impact on feminist literature.",
#     "short_review": "Melodramatic."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "b113c266-e5d3-47fd-92ab-6112915d21f8",
#     "book_rating": 4,
#     "book_review": "Tess of the d'Urbervilles is a tragic yet compelling tale of innocence lost and societal injustice. Thomas Hardy's poetic prose and vivid descriptions bring the English countryside to life.",
#     "short_review": "Tragic yet compelling."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "b113c266-e5d3-47fd-92ab-6112915d21f8",
#     "book_rating": 3,
#     "book_review": "Tess of the d'Urbervilles is a somber novel that highlights the harsh realities faced by women in Victorian England. While Hardy's writing is beautiful, the bleakness of the story may be off-putting for some.",
#     "short_review": "Somber novel."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "b113c266-e5d3-47fd-92ab-6112915d21f8",
#     "book_rating": 5,
#     "book_review": "Tess of the d'Urbervilles is a masterpiece of English literature. Hardy's exploration of themes such as fate, morality, and the plight of women is both profound and moving. A must-read for lovers of classic literature.",
#     "short_review": "Masterpiece."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "2888a4bb-9c18-4bf5-b512-61e9c4fd659f",
#     "book_rating": 4,
#     "book_review": "The Turn of the Screw is a chilling tale that keeps you on the edge of your seat. Henry James's mastery of suspense and psychological horror makes this a classic ghost story.",
#     "short_review": "Chilling tale."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "2888a4bb-9c18-4bf5-b512-61e9c4fd659f",
#     "book_rating": 5,
#     "book_review": "The Turn of the Screw is a masterpiece of ambiguity and suspense. Henry James's exploration of the supernatural and the psychological is both gripping and thought-provoking.",
#     "short_review": "Masterpiece of ambiguity."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "2888a4bb-9c18-4bf5-b512-61e9c4fd659f",
#     "book_rating": 3,
#     "book_review": "While The Turn of the Screw has its moments of suspense, I found the ambiguity frustrating. The lack of clarity regarding the supernatural elements detracted from my enjoyment of the story.",
#     "short_review": "Frustrating ambiguity."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "2888a4bb-9c18-4bf5-b512-61e9c4fd659f",
#     "book_rating": 2,
#     "book_review": "The Turn of the Screw left me feeling underwhelmed. The pacing was slow, and the plot felt disjointed. While I appreciate its literary significance, I struggled to connect with the story.",
#     "short_review": "Underwhelming."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "dcd8068f-afad-476e-9496-be37f63b341d",
#     "book_rating": 5,
#     "book_review": "The Awakening is a powerful and poignant novel that explores themes of female independence and self-discovery. Kate Chopin's lyrical prose and insightful portrayal of Edna Pontellier's journey make this a timeless classic.",
#     "short_review": "Powerful and poignant."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "dcd8068f-afad-476e-9496-be37f63b341d",
#     "book_rating": 4,
#     "book_review": "The Awakening is a thought-provoking novel that challenges societal norms and expectations. Kate Chopin's exploration of female identity and desire is as relevant today as it was when the book was first published.",
#     "short_review": "Thought-provoking."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "dcd8068f-afad-476e-9496-be37f63b341d",
#     "book_rating": 3,
#     "book_review": "While The Awakening addresses important themes, I found the protagonist's actions to be frustrating at times. However, Chopin's exploration of women's roles in society is still relevant today.",
#     "short_review": "Frustrating protagonist."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "32ee910b-5b89-4b37-a8ae-8843dba9510d",
#     "book_rating": 4,
#     "book_review": "The Cherry Orchard is a poignant and tragicomedy that offers a profound commentary on social change and the passage of time. Anton Chekhov's characters are richly drawn, and his dialogue is sharp and insightful.",
#     "short_review": "Poignant tragicomedy."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "32ee910b-5b89-4b37-a8ae-8843dba9510d",
#     "book_rating": 5,
#     "book_review": "The Cherry Orchard is a masterpiece of Russian literature. Chekhov's exploration of themes such as class, change, and loss is both profound and timeless. A must-read for anyone interested in drama.",
#     "short_review": "Masterpiece of Russian literature."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "32ee910b-5b89-4b37-a8ae-8843dba9510d",
#     "book_rating": 3,
#     "book_review": "While The Cherry Orchard has moments of brilliance, I found some parts of the play to be slow and meandering. However, Chekhov's keen observation of human nature shines through, making it worth the read.",
#     "short_review": "Moments of brilliance."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "aab4e42b-f568-4b36-9625-fcdbcec3151d",
#     "book_rating": 4,
#     "book_review": "The Age of Innocence is a captivating novel that provides a vivid portrayal of New York society in the late 19th century. Edith Wharton's prose is elegant and her characters are intricately developed.",
#     "short_review": "Captivating portrayal."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "aab4e42b-f568-4b36-9625-fcdbcec3151d",
#     "book_rating": 5,
#     "book_review": "The Age of Innocence is a masterpiece of American literature. Wharton's exploration of love, duty, and societal expectations is both timeless and thought-provoking.",
#     "short_review": "Masterpiece of literature."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "cf407f4a-2a5d-4caa-ac4f-a2e88d626295",
#     "book_rating": 3,
#     "book_review": "In Search of Lost Time is a monumental work that delves into the intricacies of memory, time, and identity. Marcel Proust's prose is dense and philosophical, requiring patience and reflection.",
#     "short_review": "Monumental work."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "cf407f4a-2a5d-4caa-ac4f-a2e88d626295",
#     "book_rating": 2,
#     "book_review": "In Search of Lost Time is a challenging read due to its length and dense prose. While Proust's exploration of memory is profound, the narrative can be slow-paced and meandering.",
#     "short_review": "Challenging read."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "e8cecd24-15d5-4395-bf73-2dbdd8c79d6e",
#     "book_rating": 5,
#     "book_review": "The Waste Land is a groundbreaking poem that captures the disillusionment and fragmentation of the post-World War I era. T.S. Eliot's use of imagery and symbolism is masterful, making this poem a seminal work of modernist literature.",
#     "short_review": "Groundbreaking poem."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "e8cecd24-15d5-4395-bf73-2dbdd8c79d6e",
#     "book_rating": 4,
#     "book_review": "The Waste Land is a complex and thought-provoking poem that requires multiple readings to fully appreciate. Eliot's use of literary allusions and fragmented structure adds layers of meaning to the text.",
#     "short_review": "Thought-provoking poem."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "4011081b-fe69-48fc-b938-1b4afeb61d0a",
#     "book_rating": 4,
#     "book_review": "The Stranger is a compelling existential novel that challenges conventional notions of morality and identity. Albert Camus's sparse prose and detached narration create an atmosphere of absurdity and alienation.",
#     "short_review": "Compelling existential novel."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "4011081b-fe69-48fc-b938-1b4afeb61d0a",
#     "book_rating": 3,
#     "book_review": "While The Stranger offers an interesting exploration of existential themes, I found the protagonist's detachment to be off-putting at times. However, Camus's writing style is undeniably impactful.",
#     "short_review": "Interesting exploration."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "588a4ec6-e7bd-451d-bfb6-44460683bb10",
#     "book_rating": 4,
#     "book_review": "Waiting for Godot is a thought-provoking play that explores themes of existentialism and the human condition. Samuel Beckett's minimalist style and absurdist dialogue create a unique theatrical experience.",
#     "short_review": "Thought-provoking play."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "588a4ec6-e7bd-451d-bfb6-44460683bb10",
#     "book_rating": 5,
#     "book_review": "Waiting for Godot is a masterpiece of modern theater. Beckett's exploration of the futility of human existence is both profound and darkly humorous. A must-read for anyone interested in existentialist literature.",
#     "short_review": "Masterpiece of theater."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "755dcd0e-9ed8-4879-8f69-9474e246d7ed",
#     "book_rating": 3,
#     "book_review": "On the Road is a classic novel that captures the spirit of the Beat Generation. Jack Kerouac's spontaneous prose and vivid descriptions of the American landscape make this a compelling read, although the lack of a cohesive plot may deter some readers.",
#     "short_review": "Captures the Beat spirit."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "755dcd0e-9ed8-4879-8f69-9474e246d7ed",
#     "book_rating": 2,
#     "book_review": "On the Road is an overrated novel that glorifies aimless wanderlust. While Kerouac's prose captures the spontaneity of the Beat Generation, the lack of character development and coherent plot make it a frustrating read.",
#     "short_review": "Overrated wanderlust."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "105a4621-d03d-46d9-a297-9f7e08f68c96",
#     "book_rating": 4,
#     "book_review": "Naked Lunch is a challenging yet rewarding novel that pushes the boundaries of traditional narrative structure. William S. Burroughs's surrealistic prose and vivid imagery create a disturbing but fascinating exploration of addiction and alienation.",
#     "short_review": "Challenging but rewarding."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "105a4621-d03d-46d9-a297-9f7e08f68c96",
#     "book_rating": 5,
#     "book_review": "Naked Lunch is a groundbreaking work of literature that defies categorization. Burroughs's stream-of-consciousness style and surrealistic imagery create a hallucinatory experience that challenges the reader's perceptions.",
#     "short_review": "Groundbreaking literature."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "308c5307-f281-4d97-914f-d73529f1c436",
#     "book_rating": 5,
#     "book_review": "Atonement is a beautifully written novel that explores the complexities of guilt, forgiveness, and redemption. Ian McEwan's prose is elegant and evocative, drawing the reader into the lives of the characters and their interconnected stories.",
#     "short_review": "Beautifully written."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "308c5307-f281-4d97-914f-d73529f1c436",
#     "book_rating": 4,
#     "book_review": "Atonement is a captivating novel that explores the consequences of a single lie. McEwan's masterful storytelling and rich character development make this a compelling read from start to finish.",
#     "short_review": "Captivating story."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "ec9bf649-1ad2-41eb-b264-bd10c80687ee",
#     "book_rating": 3,
#     "book_review": "The English Patient is a well-written novel with beautiful prose and vivid descriptions of wartime Europe. However, the nonlinear narrative structure may confuse some readers and detract from the overall enjoyment of the story.",
#     "short_review": "Well-written but confusing."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "a2663654-96bf-44f4-8285-01f8d61a2193",
#     "book_rating": 5,
#     "book_review": "The Sense of an Ending is a thought-provoking and introspective novel that explores memory, identity, and the passage of time. Julian Barnes's writing is sharp and insightful, leaving a lasting impression on the reader.",
#     "short_review": "Thought-provoking."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "144c7663-377a-42b2-a074-578a1e32cb8d",
#     "book_rating": 4,
#     "book_review": "The Unbearable Lightness of Being is a philosophical novel that delves into the complexities of love, identity, and existence. Milan Kundera's writing style is both poetic and thought-provoking, making this a compelling read for those who enjoy introspective literature.",
#     "short_review": "Poetic and thought-provoking."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "179fcde5-031d-401c-99e1-75d7858c1668",
#     "book_rating": 2,
#     "book_review": "Infinite Jest is a challenging and ambitious novel that explores various themes such as addiction, entertainment, and the search for meaning. However, its nonlinear narrative structure and extensive footnotes may deter some readers from fully engaging with the story.",
#     "short_review": "Challenging but not engaging."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "4d4915f8-ef78-482b-a865-7f31ab798c9a",
#     "book_rating": 5,
#     "book_review": "The Tale of Genji is a masterpiece of Japanese literature, offering a fascinating glimpse into the courtly life of Heian-era Japan. Murasaki Shikibu's vivid descriptions and intricate characterizations make this epic tale a timeless classic that continues to captivate readers centuries after its initial publication.",
#     "short_review": "Timeless classic."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "4d4915f8-ef78-482b-a865-7f31ab798c9a",
#     "book_rating": 4,
#     "book_review": "The Tale of Genji is a rich and immersive reading experience that transports readers to a different time and place. Murasaki Shikibu's narrative skill and attention to detail bring the characters and settings to life, making it a must-read for fans of classic literature.",
#     "short_review": "Rich and immersive."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "92bbd1f2-069b-4828-bd02-6f6afe3de195",
#     "book_rating": 4,
#     "book_review": "A Room with a View is a delightful novel that explores themes of love, social class, and freedom. E.M. Forster's writing is both charming and insightful, making this book a timeless classic that continues to resonate with readers today.",
#     "short_review": "Charming and insightful."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "f6634faa-4159-41a0-9d6e-20f3d51a27f7",
#     "book_rating": 3,
#     "book_review": "The End of the Affair is a poignant exploration of love, loss, and redemption. Graham Greene's writing is evocative and thought-provoking, but some readers may find the pacing slow and the plot predictable.",
#     "short_review": "Poignant but slow pacing."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "cdcadae9-09a4-4820-892a-8a2e28f35ddb",
#     "book_rating": 5,
#     "book_review": "Henderson the Rain King is a wild and whimsical adventure that defies categorization. Saul Bellow's vivid prose and eccentric characters make this novel a captivating read from start to finish.",
#     "short_review": "Wild and whimsical."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "92bbd1f2-069b-4828-bd02-6f6afe3de195",
#     "book_rating": 4,
#     "book_review": "A Room with a View is a beautifully written novel that transports readers to the idyllic landscapes of Italy. E.M. Forster's exploration of romance and societal expectations is both poignant and thought-provoking.",
#     "short_review": "Beautifully written."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "37d2da2f-1a3b-4a01-ab38-162100a833af",
#     "book_rating": 4,
#     "book_review": "A Good Man Is Hard to Find is a gripping collection of short stories that delves into the complexities of human nature. Flannery O'Connor's writing is both haunting and insightful, leaving a lasting impression on readers.",
#     "short_review": "Haunting and insightful."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "37d2da2f-1a3b-4a01-ab38-162100a833af",
#     "book_rating": 3,
#     "book_review": "A Good Man Is Hard to Find offers a glimpse into the darker aspects of life through its intriguing characters and unexpected plot twists. While some stories are more engaging than others, Flannery O'Connor's masterful storytelling shines throughout.",
#     "short_review": "Engaging but uneven."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "37d2da2f-1a3b-4a01-ab38-162100a833af",
#     "book_rating": 5,
#     "book_review": "A Good Man Is Hard to Find is a literary masterpiece that skillfully blends elements of humor, tragedy, and morality. Flannery O'Connor's vivid imagery and sharp wit make this collection a must-read for fans of Southern Gothic fiction.",
#     "short_review": "Masterful and vivid."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "17aa4df7-f547-46d4-a60d-ddb68d89ce2d",
#     "book_rating": 3,
#     "book_review": "Death of a Naturalist offers a lyrical exploration of nature and childhood memories. Seamus Heaney's poetry is evocative, but some readers may find the themes repetitive.",
#     "short_review": "Lyrical but repetitive."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "17aa4df7-f547-46d4-a60d-ddb68d89ce2d",
#     "book_rating": 5,
#     "book_review": "Death of a Naturalist is a poignant collection of poems that captures the beauty and brutality of the natural world. Seamus Heaney's imagery is vivid, and his exploration of Irish rural life is both captivating and moving.",
#     "short_review": "Captivating and moving."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "17aa4df7-f547-46d4-a60d-ddb68d89ce2d",
#     "book_rating": 4,
#     "book_review": "Death of a Naturalist is a compelling collection of poems that skillfully juxtaposes the beauty and harshness of nature. Seamus Heaney's poetic language transports readers to the Irish countryside, evoking a sense of nostalgia and wonder.",
#     "short_review": "Compelling and nostalgic."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "61e48b82-ca50-4e17-9b66-7b007eb2218c",
#     "book_rating": 4,
#     "book_review": "Omeros is an epic poem that weaves together themes of history, identity, and mythology. Derek Walcott's lyrical prose transports readers to the Caribbean, offering a rich and immersive reading experience.",
#     "short_review": "Rich and immersive."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "61e48b82-ca50-4e17-9b66-7b007eb2218c",
#     "book_rating": 5,
#     "book_review": "Omeros is a breathtaking work of literature that blends mythology with the harsh realities of Caribbean life. Derek Walcott's poetic language and vivid imagery create a mesmerizing narrative that stays with the reader long after the final page.",
#     "short_review": "Breathtaking and mesmerizing."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "61e48b82-ca50-4e17-9b66-7b007eb2218c",
#     "book_rating": 3,
#     "book_review": "Omeros is a complex and ambitious poem that explores themes of identity, colonization, and cultural heritage. While Derek Walcott's writing is undeniably beautiful, the structure of the poem can be difficult to follow at times.",
#     "short_review": "Beautiful but challenging."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "51fab1f5-e7c9-47fc-965a-15027bb7c2d3",
#     "book_rating": 4,
#     "book_review": "The Magic Mountain is a thought-provoking novel that explores complex philosophical ideas within the confines of a sanatorium. Thomas Mann's intricate prose and rich character development make this book a rewarding but challenging read.",
#     "short_review": "Thought-provoking and rewarding."
#   },
#   {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "51fab1f5-e7c9-47fc-965a-15027bb7c2d3",
#     "book_rating": 5,
#     "book_review": "The Magic Mountain is an immersive journey into the human psyche, set against the backdrop of a tuberculosis sanatorium. Thomas Mann's prose is dense but rewarding, offering profound insights into life, death, and the search for meaning.",
#     "short_review": "Immersive and profound."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "51fab1f5-e7c9-47fc-965a-15027bb7c2d3",
#     "book_rating": 3,
#     "book_review": "The Magic Mountain is a challenging yet ultimately rewarding novel that delves into the complexities of human existence. While Thomas Mann's philosophical musings can be dense at times, the depth of his insights makes this book a worthwhile read.",
#     "short_review": "Challenging but worthwhile."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "d3a4f48f-8243-49e3-8250-452fb38225a1",
#     "book_rating": 5,
#     "book_review": "Ficciones is a mesmerizing collection of short stories that showcases Jorge Luis Borges' unparalleled imagination and intellect. Each story is a labyrinth of ideas, inviting readers to explore philosophical concepts and existential dilemmas.",
#     "short_review": "Mesmerizing and thought-provoking."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "d3a4f48f-8243-49e3-8250-452fb38225a1",
#     "book_rating": 4,
#     "book_review": "Ficciones is a literary masterpiece that blurs the lines between reality and fiction. Jorge Luis Borges' innovative narrative techniques and intricate plots make this collection a must-read for lovers of mind-bending literature.",
#     "short_review": "Innovative and mind-bending."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "d3a4f48f-8243-49e3-8250-452fb38225a1",
#     "book_rating": 3,
#     "book_review": "Ficciones is an intellectually stimulating collection of stories that challenges readers to question the nature of reality. While Jorge Luis Borges' writing is undeniably brilliant, some stories may feel inaccessible to casual readers.",
#     "short_review": "Intellectually stimulating but inaccessible."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "c78ebd24-9e96-4e84-9843-7016a9602323",
#     "book_rating": 4,
#     "book_review": "Invisible Cities is a breathtaking exploration of imagination and urban landscapes. Italo Calvino's prose is lyrical and evocative, painting vivid portraits of imaginary cities that linger in the mind long after the book is finished.",
#     "short_review": "Breathtaking and vivid."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "c78ebd24-9e96-4e84-9843-7016a9602323",
#     "book_rating": 5,
#     "book_review": "Invisible Cities is a literary marvel that transcends the boundaries of traditional storytelling. Italo Calvino's imaginative vision and poetic language create a mesmerizing journey through fantastical cities that defy logic and convention.",
#     "short_review": "Mesmerizing and poetic."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "c78ebd24-9e96-4e84-9843-7016a9602323",
#     "book_rating": 3,
#     "book_review": "Invisible Cities is an ambitious work that showcases Italo Calvino's boundless creativity. While some sections are beautifully crafted, others may feel disjointed or overly abstract, making the reading experience uneven.",
#     "short_review": "Ambitious but uneven."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "9b5427ed-badb-4e4e-82f3-478ab7d8e0c4",
#     "book_rating": 4,
#     "book_review": "Blindness is a haunting exploration of human nature and society's response to crisis. Jose Saramago's stark prose and relentless narrative pull readers into a dystopian world where the loss of sight reveals the darkness within us all.",
#     "short_review": "Haunting and relentless."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "9b5427ed-badb-4e4e-82f3-478ab7d8e0c4",
#     "book_rating": 5,
#     "book_review": "Blindness is a powerful allegory that exposes the fragility of civilization and the resilience of the human spirit. Jose Saramago's unflinching portrayal of societal collapse is both harrowing and thought-provoking, leaving a profound impact on readers.",
#     "short_review": "Powerful and thought-provoking."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "9b5427ed-badb-4e4e-82f3-478ab7d8e0c4",
#     "book_rating": 3,
#     "book_review": "Blindness is a disturbing yet compelling novel that explores the darkest depths of human nature. While Jose Saramago's writing is undeniably powerful, the relentless bleakness of the narrative may be overwhelming for some readers.",
#     "short_review": "Disturbing but powerful."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "fabe6dd1-fa38-457c-9f9d-6676ef7002d6",
#     "book_rating": 4,
#     "book_review": "If This Is a Man is a harrowing memoir that offers a stark portrayal of survival and resilience in the face of unimaginable suffering. Primo Levi's unflinching honesty and introspection make this book a haunting testament to the human spirit.",
#     "short_review": "Harrowing and honest."
#   },
#     {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "507a7709-0beb-4795-8ac8-de908803bbaa",
#     "book_rating": 5,
#     "book_review": "The Name of the Rose is a captivating historical mystery that combines elements of theology, philosophy, and suspense. Umberto Eco's meticulous attention to detail and rich character development make this novel a must-read for fans of intelligent fiction.",
#     "short_review": "Captivating and intelligent."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "507a7709-0beb-4795-8ac8-de908803bbaa",
#     "book_rating": 4,
#     "book_review": "The Name of the Rose is an intriguing blend of historical fiction and murder mystery. Umberto Eco's erudite prose and intricate plot keep readers engaged until the very end, though some may find the theological discussions overwhelming at times.",
#     "short_review": "Intriguing but overwhelming."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "507a7709-0beb-4795-8ac8-de908803bbaa",
#     "book_rating": 3,
#     "book_review": "The Name of the Rose is an ambitious novel that delves deep into the realms of history, religion, and philosophy. While Umberto Eco's prose is undeniably masterful, the dense philosophical discussions may alienate some readers.",
#     "short_review": "Ambitious but alienating."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "507a7709-0beb-4795-8ac8-de908803bbaa",
#     "book_rating": 4,
#     "book_review": "The Name of the Rose is a thought-provoking novel that challenges readers to explore complex themes of faith, knowledge, and power. Umberto Eco's narrative skill and historical depth create an immersive reading experience that lingers long after the book is finished.",
#     "short_review": "Thought-provoking and immersive."
#   },
#   {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "66eece62-7a93-46a3-85c4-4ba15e646bd0",
#     "book_rating": 3,
#     "book_review": "White Teeth is a sprawling epic that navigates themes of identity, culture, and belonging. Zadie Smith's ambitious storytelling and vivid characterizations make this novel a compelling read, although some may find its length and multiple narratives overwhelming.",
#     "short_review": "Ambitious but overwhelming."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "66eece62-7a93-46a3-85c4-4ba15e646bd0",
#     "book_rating": 4,
#     "book_review": "White Teeth is a brilliant exploration of multiculturalism and the complexities of modern life. Zadie Smith's sharp wit and keen observation create a vibrant tapestry of characters and stories that resonate with readers from diverse backgrounds.",
#     "short_review": "Brilliant and vibrant."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "66eece62-7a93-46a3-85c4-4ba15e646bd0",
#     "book_rating": 5,
#     "book_review": "White Teeth is an exhilarating literary journey that captures the essence of multicultural London. Zadie Smith's sharp social commentary and richly drawn characters make this novel a true masterpiece of modern literature.",
#     "short_review": "Exhilarating and masterful."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "66eece62-7a93-46a3-85c4-4ba15e646bd0",
#     "book_rating": 3,
#     "book_review": "White Teeth is a complex and ambitious novel that explores the intricacies of identity and culture. While Zadie Smith's writing is undeniably powerful, the sprawling narrative and multitude of characters may overwhelm some readers.",
#     "short_review": "Complex but overwhelming."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "1e0c4f7a-c46c-4dad-97be-06061010c73a",
#     "book_rating": 4,
#     "book_review": "My Brilliant Friend is a captivating exploration of friendship, identity, and societal expectations. Elena Ferrante's richly textured prose and intimate portrayal of female friendship make this novel a poignant and unforgettable read.",
#     "short_review": "Captivating and poignant."
#   },
#     {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "88814018-1039-4f93-aeac-dda2e321b287",
#     "book_rating": 5,
#     "book_review": "The Underground Railroad is a powerful and moving novel that offers a gripping portrayal of the horrors of slavery in America. Colson Whitehead's writing is both haunting and lyrical, making this book a must-read for anyone interested in American history.",
#     "short_review": "Powerful and moving."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "88814018-1039-4f93-aeac-dda2e321b287",
#     "book_rating": 4,
#     "book_review": "The Underground Railroad is a compelling and thought-provoking novel that explores the harsh realities of slavery in America. Colson Whitehead's vivid storytelling and well-developed characters make this book an engrossing read from start to finish.",
#     "short_review": "Compelling and thought-provoking."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "88814018-1039-4f93-aeac-dda2e321b287",
#     "book_rating": 3,
#     "book_review": "The Underground Railroad is an important and impactful novel that sheds light on a dark chapter of American history. While Colson Whitehead's prose is undeniably powerful, the nonlinear narrative may be confusing for some readers.",
#     "short_review": "Important but confusing."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "88814018-1039-4f93-aeac-dda2e321b287",
#     "book_rating": 5,
#     "book_review": "The Underground Railroad is a masterfully crafted novel that vividly captures the struggles of enslaved people seeking freedom. Colson Whitehead's storytelling prowess and vivid imagery make this book a profound and unforgettable read.",
#     "short_review": "Masterfully crafted and profound."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "980a7310-f81e-4e5f-9cde-ee0a440c0335",
#     "book_rating": 4,
#     "book_review": "The Second Sex is a groundbreaking work that remains relevant in its exploration of gender and society. Simone de Beauvoir's thorough analysis and critical insights make this book essential reading for anyone interested in feminist theory.",
#     "short_review": "Groundbreaking and relevant."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "980a7310-f81e-4e5f-9cde-ee0a440c0335",
#     "book_rating": 3,
#     "book_review": "The Second Sex offers a comprehensive examination of the status of women in society, but its dense philosophical prose may be challenging for some readers to digest. Simone de Beauvoir's insights, however, are invaluable for understanding the complexities of gender.",
#     "short_review": "Comprehensive but challenging."
#   },
#   {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "980a7310-f81e-4e5f-9cde-ee0a440c0335",
#     "book_rating": 5,
#     "book_review": "The Second Sex is an essential feminist text that offers a profound analysis of the oppression of women throughout history. Simone de Beauvoir's eloquent prose and incisive critique make this book a timeless classic that continues to inspire generations of readers.",
#     "short_review": "Essential and timeless."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "4f7ceba9-7c72-44dc-8e18-28b2fc3a4553",
#     "book_rating": 4,
#     "book_review": "Charlie and the Chocolate Factory is a delightful and whimsical tale that sparks the imagination. Roald Dahl's colorful characters and imaginative world-building make this book a timeless classic for readers of all ages.",
#     "short_review": "Delightful and whimsical."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "cac758ad-3381-4182-a6ea-0022b083495a",
#     "book_rating": 4,
#     "book_review": "The Talented Mr. Ripley is a gripping psychological thriller that keeps you on the edge of your seat. Patricia Highsmith's masterful storytelling and complex characters make this book a must-read for fans of the genre.",
#     "short_review": "Gripping and masterful."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "cac758ad-3381-4182-a6ea-0022b083495a",
#     "book_rating": 3,
#     "book_review": "The Talented Mr. Ripley is an intriguing novel with a unique premise, but the pacing may feel slow for some readers. Patricia Highsmith's exploration of identity and morality, however, is thought-provoking.",
#     "short_review": "Intriguing but slow-paced."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "cac758ad-3381-4182-a6ea-0022b083495a",
#     "book_rating": 5,
#     "book_review": "The Talented Mr. Ripley is a masterpiece of suspense and psychological tension. Patricia Highsmith's portrayal of Tom Ripley's descent into amorality is both chilling and captivating, making this book an unforgettable read.",
#     "short_review": "Masterpiece of suspense."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "cac758ad-3381-4182-a6ea-0022b083495a",
#     "book_rating": 4,
#     "book_review": "The Talented Mr. Ripley is a riveting and unsettling thriller that delves into the depths of human nature. Patricia Highsmith's exploration of obsession and deception is as thought-provoking as it is chilling.",
#     "short_review": "Riveting and unsettling."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "744ebc9e-f9bc-436e-8fbc-358b21caf417",
#     "book_rating": 5,
#     "book_review": "Night is a powerful and haunting memoir that offers a firsthand account of the horrors of the Holocaust. Elie Wiesel's prose is both eloquent and deeply moving, making this book an essential read for understanding the human experience during wartime.",
#     "short_review": "Powerful and haunting."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "744ebc9e-f9bc-436e-8fbc-358b21caf417",
#     "book_rating": 4,
#     "book_review": "Night is a harrowing and unforgettable memoir that vividly captures the atrocities of the Holocaust. Elie Wiesel's firsthand account of survival and loss serves as a stark reminder of the resilience of the human spirit.",
#     "short_review": "Harrowing and unforgettable."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "bcbec230-2e3f-42fc-86ad-77888be36f86",
#     "book_rating": 3,
#     "book_review": "Where the Wild Things Are is a whimsical and imaginative children's book that sparks the imagination. Maurice Sendak's illustrations are charming, but the story may be too simplistic for older readers.",
#     "short_review": "Whimsical but simplistic."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "bcbec230-2e3f-42fc-86ad-77888be36f86",
#     "book_rating": 5,
#     "book_review": "Where the Wild Things Are is a timeless classic that celebrates the power of imagination. Maurice Sendak's whimsical illustrations and heartfelt story resonate with readers of all ages, making this book a beloved favorite.",
#     "short_review": "Timeless classic."
#   },
#     {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "13e2d36c-fca8-4efc-8612-d12bd473c31c",
#     "book_rating": 5,
#     "book_review": "In the Night Kitchen is a delightful children's book with stunning illustrations and a whimsical storyline. Maurice Sendak's creativity shines through in this imaginative tale that captures the magic of childhood.",
#     "short_review": "Delightful and imaginative."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "13e2d36c-fca8-4efc-8612-d12bd473c31c",
#     "book_rating": 4,
#     "book_review": "In the Night Kitchen is a charming book that sparks the imagination and encourages creativity. Maurice Sendak's illustrations are captivating, and the story is both entertaining and educational.",
#     "short_review": "Charming and captivating."
#   },
#   {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "13e2d36c-fca8-4efc-8612-d12bd473c31c",
#     "book_rating": 3,
#     "book_review": "In the Night Kitchen is an interesting book with unique illustrations, but the storyline may be confusing for young readers. Maurice Sendak's creativity is evident, but the execution falls short in some aspects.",
#     "short_review": "Interesting but confusing."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "13e2d36c-fca8-4efc-8612-d12bd473c31c",
#     "book_rating": 5,
#     "book_review": "In the Night Kitchen is a classic children's book that stands the test of time. Maurice Sendak's imaginative storytelling and vibrant illustrations make this book a must-read for children of all ages.",
#     "short_review": "Classic and vibrant."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "53e2bf04-958a-49c4-a21a-191a3e8a5e1d",
#     "book_rating": 5,
#     "book_review": "The Giving Tree is a heartwarming story that teaches valuable lessons about selflessness and generosity. Shel Silverstein's simple yet profound tale resonates with readers of all ages, making it a timeless classic.",
#     "short_review": "Heartwarming and profound."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "53e2bf04-958a-49c4-a21a-191a3e8a5e1d",
#     "book_rating": 4,
#     "book_review": "The Giving Tree is a touching story that explores themes of love and sacrifice. Shel Silverstein's poignant illustrations and simple prose make this book a memorable read for both children and adults.",
#     "short_review": "Touching and memorable."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "53e2bf04-958a-49c4-a21a-191a3e8a5e1d",
#     "book_rating": 3,
#     "book_review": "The Giving Tree is a bittersweet story with beautiful illustrations, but the narrative may feel overly simplistic for adult readers. Shel Silverstein's message of selflessness is clear, but the execution lacks depth.",
#     "short_review": "Bittersweet with beautiful illustrations."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "048fe0a4-b73f-41b0-8c70-e82c7dd9c401",
#     "book_rating": 4,
#     "book_review": "Where the Sidewalk Ends is a whimsical collection of poems that delights readers with its imaginative language and playful illustrations. Shel Silverstein's wit and charm shine through in each poem, making this book a joy to read.",
#     "short_review": "Whimsical and delightful."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "048fe0a4-b73f-41b0-8c70-e82c7dd9c401",
#     "book_rating": 5,
#     "book_review": "Where the Sidewalk Ends is a timeless classic that sparks the imagination and encourages creativity in readers of all ages. Shel Silverstein's whimsical poems and illustrations captivate the heart and mind, making this book a beloved favorite.",
#     "short_review": "Timeless classic."
#   },
#     {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "55f429ca-96a2-4824-9d4c-cdbe1d0fee8a",
#     "book_rating": 4,
#     "book_review": "The Angel's Game is a captivating thriller with intricate plot twists and well-developed characters. Carlos Ruiz Zafón's storytelling keeps readers on the edge of their seats until the very end.",
#     "short_review": "Captivating thriller."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "55f429ca-96a2-4824-9d4c-cdbe1d0fee8a",
#     "book_rating": 5,
#     "book_review": "The Angel's Game is a masterpiece of suspense and mystery. Carlos Ruiz Zafón's writing is mesmerizing, and the story unfolds with unexpected twists and turns that keep readers guessing until the end.",
#     "short_review": "Masterpiece of suspense."
#   },
#   {
#     "user_id": "7c7a29c9-a713-440b-9b85-eb5033f02641",
#     "book_id": "55f429ca-96a2-4824-9d4c-cdbe1d0fee8a",
#     "book_rating": 3,
#     "book_review": "The Angel's Game is an intriguing novel with a complex plot and vivid imagery. While the story keeps readers engaged, some may find the pacing slow at times.",
#     "short_review": "Intriguing but slow-paced."
#   },
#   {
#     "user_id": "ca1f6b8e-fa79-4d48-8cbc-dd0ef439327e",
#     "book_id": "55f429ca-96a2-4824-9d4c-cdbe1d0fee8a",
#     "book_rating": 4,
#     "book_review": "The Angel's Game is a compelling read that immerses readers into a world of mystery and intrigue. Carlos Ruiz Zafón's descriptive prose and intricate plot make this book a must-read for fans of suspense.",
#     "short_review": "Compelling and immersive."
#   },
#   {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "db373c49-8d18-4e2c-83a4-8d174decd087",
#     "book_rating": 2,
#     "book_review": "The Da Vinci Code is an overrated novel that fails to live up to its hype. While the premise is intriguing, the execution feels contrived, and the writing lacks depth.",
#     "short_review": "Overrated and contrived."
#   },
#   {
#     "user_id": "9c1b9d38-b2df-4a79-8091-8ef8fa821c88",
#     "book_id": "db373c49-8d18-4e2c-83a4-8d174decd087",
#     "book_rating": 3,
#     "book_review": "The Da Vinci Code is an entertaining thriller that keeps readers engaged with its fast-paced plot and historical mysteries. While not groundbreaking, it's a decent read for fans of the genre.",
#     "short_review": "Entertaining but not groundbreaking."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "db373c49-8d18-4e2c-83a4-8d174decd087",
#     "book_rating": 4,
#     "book_review": "The Da Vinci Code is a gripping page-turner that seamlessly blends history, religion, and conspiracy. Dan Brown's storytelling keeps readers hooked from start to finish, making it a thrilling read.",
#     "short_review": "Gripping page-turner."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "db373c49-8d18-4e2c-83a4-8d174decd087",
#     "book_rating": 5,
#     "book_review": "The Da Vinci Code is a riveting adventure that combines mystery, history, and suspense seamlessly. Dan Brown's storytelling prowess shines in this thrilling tale that keeps readers guessing until the very end.",
#     "short_review": "Riveting adventure."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "dca253be-4e17-4028-ab11-85fb94f33e98",
#     "book_rating": 4,
#     "book_review": "Angels & Demons is a fast-paced thriller that keeps readers on the edge of their seats. Dan Brown's intricate plot and suspenseful writing make this book a thrilling ride from start to finish.",
#     "short_review": "Fast-paced thriller."
#   },
#     {
#     "user_id": "8410ebc7-bddd-4cff-a651-24b74f193192",
#     "book_id": "7b122235-11f9-41f2-80e7-da776e1813f2",
#     "book_rating": 5,
#     "book_review": "The Dutch House is a beautifully written novel that explores themes of family, loss, and resilience. Ann Patchett's storytelling draws readers into the lives of the characters, making it a compelling and emotional read.",
#     "short_review": "Beautifully written."
#   },
#   {
#     "user_id": "550de341-e5c4-486f-b087-5ef77ff3a72b",
#     "book_id": "7b122235-11f9-41f2-80e7-da776e1813f2",
#     "book_rating": 4,
#     "book_review": "The Dutch House is a poignant story about the complexities of family dynamics. Ann Patchett's prose is elegant and evocative, creating a richly immersive reading experience.",
#     "short_review": "Poignant and immersive."
#   },
#   {
#     "user_id": "671b88b5-2cb1-43ff-9b2d-c19c6e319ef7",
#     "book_id": "7b122235-11f9-41f2-80e7-da776e1813f2",
#     "book_rating": 3,
#     "book_review": "The Dutch House offers a nuanced portrayal of familial relationships and their lasting impact. While the writing is skillful, the pacing may feel slow for some readers.",
#     "short_review": "Nuanced portrayal."
#   },
#   {
#     "user_id": "7bb8095f-c1a8-4307-b74f-2affe40bae4b",
#     "book_id": "7b122235-11f9-41f2-80e7-da776e1813f2",
#     "book_rating": 5,
#     "book_review": "The Dutch House is a masterfully crafted novel that delves deep into the complexities of human emotion. Ann Patchett's prose is both elegant and moving, making it a truly unforgettable read.",
#     "short_review": "Masterfully crafted."
#   },
#   {
#     "user_id": "3e4992a5-bde8-4df2-ae06-051d0b7a1805",
#     "book_id": "46016ef3-cc7c-4439-9aec-580fddc43a58",
#     "book_rating": 2,
#     "book_review": "Commonwealth is a disappointing read with underdeveloped characters and a disjointed narrative. While the premise had potential, the execution fell short of expectations.",
#     "short_review": "Disappointing and underdeveloped."
#   },
#   {
#     "user_id": "85e505f3-d55e-45cb-8d38-f91ae9164d17",
#     "book_id": "46016ef3-cc7c-4439-9aec-580fddc43a58",
#     "book_rating": 3,
#     "book_review": "Commonwealth is an interesting exploration of family dynamics and secrets. While the storytelling is engaging, some may find the nonlinear narrative confusing.",
#     "short_review": "Engaging but confusing."
#   },
#   {
#     "user_id": "de223b1f-28ef-4921-b846-0613747e1cee",
#     "book_id": "46016ef3-cc7c-4439-9aec-580fddc43a58",
#     "book_rating": 4,
#     "book_review": "Commonwealth is a thought-provoking novel that skillfully weaves together multiple perspectives and timelines. Ann Patchett's storytelling prowess shines in this captivating exploration of family and forgiveness.",
#     "short_review": "Thought-provoking and captivating."
#   },
# ]



# reviews_data = [
#     {"user_id": 1, "book_id": 1, "book_rating": 5, "book_review": "A stunning work that envisions a future dystopia. Orwell's '1984' is a masterpiece of political commentary."},
#     {"user_id": 1, "book_id": 2, "book_rating": 4, "book_review": "Animal Farm is a classic allegory with powerful messages. It is relevant even today."},
#     {"user_id": 1, "book_id": 3, "book_rating": 3, "book_review": "To the Lighthouse provides an insightful exploration of human relationships, emotions, and the passage of time."},
#     {"user_id": 1, "book_id": 4, "book_rating": 4, "book_review": "Mrs Dalloway brilliantly encapsulates a single day in London, filled with rich internal monologues and streams of consciousness."},
#     {"user_id": 1, "book_id": 5, "book_rating": 5, "book_review": "The Old Man and The Sea is a tale of struggle and resilience. Hemingway's prose is powerful and evocative."},
#     {"user_id": 1, "book_id": 6, "book_rating": 4, "book_review": "A Farewell to Arms delivers an intense portrayal of love and war. Hemingway's writing is raw and beautiful."},
#     {"user_id": 1, "book_id": 7, "book_rating": 3, "book_review": "Ulysses is challenging yet rewarding. Joyce's work requires patience, but it's a journey worth undertaking."},
#     {"user_id": 1, "book_id": 8, "book_rating": 4, "book_review": "Finnegans Wake is complex and dense, but its linguistic inventiveness is a testament to Joyce's genius."},
#     {"user_id": 1, "book_id": 9, "book_rating": 4, "book_review": "Wuthering Heights is a haunting tale of love and obsession. Bronte's characters are unforgettable."},
#     {"user_id": 1, "book_id": 10, "book_rating": 5, "book_review": "Pride and Prejudice is an enduring classic. Austen's wit and character development are remarkable."},
#     {"user_id": 1, "book_id": 11, "book_rating": 4, "book_review": "Emma is a lively comedy of manners that explores societal constraints and human nature."},
#     {"user_id": 1, "book_id": 12, "book_rating": 3, "book_review": "Great Expectations is a moving coming-of-age story, filled with memorable characters and sharp social critique."},
#     {"user_id": 1, "book_id": 13, "book_rating": 4, "book_review": "Oliver Twist presents a vivid picture of London's criminal underworld. Dickens' storytelling is masterful."},
#     {"user_id": 1, "book_id": 14, "book_rating": 5, "book_review": "Adventures of Huckleberry Finn is both a great adventure story and a powerful social commentary."},
#     {"user_id": 1, "book_id": 15, "book_rating": 4, "book_review": "The Adventures of Tom Sawyer is a delightful portrayal of boyhood along the Mississippi River."},
#     {"user_id": 1, "book_id": 16, "book_rating": 5, "book_review": "To Kill a Mockingbird is a masterpiece that addresses profound themes of morality, prejudice, and the loss of innocence."},
#     {"user_id": 1, "book_id": 17, "book_rating": 3, "book_review": "Go Set a Watchman presents a more complex, but perhaps less appealing, version of Atticus Finch. It's a challenging companion piece to To Kill a Mockingbird."},
#     {"user_id": 1, "book_id": 18, "book_rating": 4, "book_review": "The Catcher in the Rye is a definitive work on adolescent alienation. Salinger's narrative voice is uniquely compelling."},
#     {"user_id": 1, "book_id": 19, "book_rating": 4, "book_review": "Nine Stories showcases Salinger's skill in writing short fiction. His characters and dialogues are vivid and memorable."},
#     {"user_id": 1, "book_id": 20, "book_rating": 4, "book_review": "Franny and Zooey is a touching exploration of spiritual crisis and familial bonds. Salinger's style is immersive and engaging."},
    
    
#     {"user_id": 2, "book_id": 1, "book_rating": 5, "book_review": "Orwell's '1984' paints a chilling picture of a dystopian future. It is a powerful critique of totalitarian regimes."},
#     {"user_id": 2, "book_id": 2, "book_rating": 4, "book_review": "'Animal Farm' is a brilliant allegorical novel that showcases Orwell's insight into the mechanisms of power."},
#     {"user_id": 2, "book_id": 3, "book_rating": 3, "book_review": "While 'To the Lighthouse' by Virginia Woolf is an introspective look into characters' psyches, it's a slow read."},
#     {"user_id": 2, "book_id": 4, "book_rating": 4, "book_review": "Woolf's 'Mrs Dalloway' is a beautiful exploration of a single day in a woman's life."},
#     {"user_id": 2, "book_id": 3, "book_rating": 5, "book_review": "The Old Man and The Sea is a testament to Hemingway's talent for poignant storytelling."},
#     {"user_id": 2, "book_id": 6, "book_rating": 4, "book_review": "Hemingway's 'A Farewell to Arms' is a raw and powerful narrative of love and war."},
#     {"user_id": 2, "book_id": 7, "book_rating": 3, "book_review": "'Ulysses' is a difficult read, but the journey through its labyrinthine narrative structure is worthwhile."},
#     {"user_id": 2, "book_id": 8, "book_rating": 4, "book_review": "Interesting work by James Joyce, although it was challenging due to its experimental style."},
#     {"user_id": 2, "book_id": 9, "book_rating": 5, "book_review": "The rawness of emotions in 'Wuthering Heights' is a testament to Emily Bronte's brilliant writing."},
#     {"user_id": 2, "book_id": 10, "book_rating": 5, "book_review": "Austen's 'Pride and Prejudice' provides a detailed look into society norms and is a classic romance."},
#     {"user_id": 2, "book_id": 11, "book_rating": 4, "book_review": "Emma is Austen's finest work, with excellent character development and humorous dialogue."},
#     {"user_id": 2, "book_id": 12, "book_rating": 3, "book_review": "Although 'Great Expectations' was tough to get into, it was overall a compelling narrative by Dickens."},
#     {"user_id": 2, "book_id": 13, "book_rating": 4, "book_review": "'Oliver Twist' remains a classic with its poignant portrayal of societal injustice."},
#     {"user_id": 2, "book_id": 14, "book_rating": 5, "book_review": "'Adventures of Huckleberry Finn' is a timeless classic that combines humor, adventure, and humanism."},
#     {"user_id": 2, "book_id": 15, "book_rating": 4, "book_review": "Twain's 'The Adventures of Tom Sawyer' is a delightful read that captures the essence of childhood."},
#     {"user_id": 2, "book_id": 16, "book_rating": 5, "book_review": "'To Kill a Mockingbird' is an enduring tale of morality and racial inequality. It's a must-read."},
#     {"user_id": 2, "book_id": 17, "book_rating": 3, "book_review": "'Go Set a Watchman' is a fascinating, though controversial, follow-up to 'To Kill a Mockingbird'."},
#     {"user_id": 2, "book_id": 18, "book_rating": 4, "book_review": "Salinger's 'The Catcher in the Rye' is an emotional journey through the protagonist's psyche."},
#     {"user_id": 2, "book_id": 19, "book_rating": 4, "book_review": "'Nine Stories' by Salinger showcases his ability to encapsulate profound themes within simple narratives."},
#     {"user_id": 2, "book_id": 20, "book_rating": 4, "book_review": "'Franny and Zooey' is a gripping exploration of religious curiosity and the dynamics of family relationships."},

    
#     {"user_id": 3, "book_id": 1, "book_rating": 5, "book_review": "A stunning work that envisions a future dystopia. Orwell's '1984' is a masterpiece of political commentary."},
#     {"user_id": 3, "book_id": 2, "book_rating": 4, "book_review": "Animal Farm beautifully demonstrates the corruption of revolution by its leaders. Orwell's satire remains relevant and impactful."},
#     {"user_id": 3, "book_id": 3, "book_rating": 5, "book_review": "To the Lighthouse is an insightful exploration of the human mind and its relationship with the outside world. A remarkable example of Woolf's stream of consciousness style."},
#     {"user_id": 3, "book_id": 4, "book_rating": 4, "book_review": "Mrs Dalloway is a beautiful and moving depiction of a day in a woman's life, a classic of modernist literature."},
#     {"user_id": 3, "book_id": 5, "book_rating": 5, "book_review": "The Old Man and The Sea is an eloquent tribute to man's resilience in the face of failure. Hemingway's simple yet powerful prose is remarkable."},
#     {"user_id": 3, "book_id": 6, "book_rating": 4, "book_review": "A Farewell to Arms provides a deeply affecting portrayal of love and war. Hemingway's writing is both heart-wrenching and beautiful."},
#     {"user_id": 3, "book_id": 7, "book_rating": 5, "book_review": "Ulysses is a challenging but rewarding read, full of innovative stylistic choices and deep, meaningful character studies."},
#     {"user_id": 3, "book_id": 8, "book_rating": 3, "book_review": "Finnegans Wake is a complex, cryptic work. Joyce's innovative use of language is both fascinating and frustrating."},
#     {"user_id": 3, "book_id": 9, "book_rating": 4, "book_review": "Wuthering Heights is a compelling tale of passion and revenge. Bronte's evocative description of the moorland setting adds to the brooding atmosphere."},
#     {"user_id": 3, "book_id": 10, "book_rating": 5, "book_review": "Pride and Prejudice is a delightful read. The characters, particularly the witty Elizabeth Bennet, are wonderfully realised."},
#     {"user_id": 3, "book_id": 11, "book_rating": 4, "book_review": "Emma is a charming novel with a wonderfully flawed protagonist. Austen's clever use of irony and social commentary is superb."},
#     {"user_id": 3, "book_id": 12, "book_rating": 5, "book_review": "Great Expectations is a classic tale of love, social mobility, and personal growth. Dickens's richly-detailed writing brings the characters to life."},
#     {"user_id": 3, "book_id": 13, "book_rating": 4, "book_review": "Oliver Twist is a stark exploration of the struggle for survival in 19th century London. A powerful and moving read."},
#     {"user_id": 3, "book_id": 14, "book_rating": 5, "book_review": "Adventures of Huckleberry Finn is an essential American novel, full of humor and wisdom. Twain's depiction of life along the Mississippi River is legendary."},
#     {"user_id": 3, "book_id": 15, "book_rating": 4, "book_review": "The Adventures of Tom Sawyer is a fun and adventurous read, capturing the essence of childhood imagination and freedom."},
#     {"user_id": 3, "book_id": 16, "book_rating": 5, "book_review": "To Kill a Mockingbird is a profound book with powerful themes of racism and innocence. An essential read for everyone."},
#     {"user_id": 3, "book_id": 17, "book_rating": 3, "book_review": "Go Set a Watchman revisits the characters of To Kill a Mockingbird, offering a more complex and less idealistic view of the issues at hand."},
#     {"user_id": 3, "book_id": 18, "book_rating": 5, "book_review": "The Catcher in the Rye is a classic coming-of-age story, capturing the angst and alienation of adolescence. Salinger's writing style is both authentic and compelling."},
#     {"user_id": 3, "book_id": 19, "book_rating": 4, "book_review": "Nine Stories is a collection of sharp and poignant short stories. Salinger's depth of characterisation in each story is masterful."},
#     {"user_id": 3, "book_id": 20, "book_rating": 4, "book_review": "Franny and Zooey is a fascinating exploration of spirituality and the human condition. Salinger's writing is introspective and illuminating."}
# ]
