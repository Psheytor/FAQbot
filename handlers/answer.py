from aiogram import Router, F
from aiogram.types import Message


router = Router()
@router.message(F.text=='1')
async def message_answer(message: Message):
    await message.reply("Задать вопросы учебного характера можно специалистам деканата факультета или института – контакты представлены [по ссылке](https://omgtu.ru/general_information/the-structure/). Получить справку об обучении можно в деканате либо в личном кабинете студента.", parse_mode="Markdown",disable_web_page_preview=True)
@router.message(F.text=='2')
async def message_answer(message: Message):
    await message.reply("Стипендия приходит в последний рабочий день месяца. О различных видах материальной поддержки подробнее [по ссылке](https://vk.com/doc182856499_608500178?hash=ccbf39d1bb0491649e&dl=b8dc4ee823cfd268c5). По всем вопросам можно обратиться в отдел молодежной политики (главный корпус ОмГТУ, кабинет Г-221) либо в группу [Портала молодежных проектов и инициатив ОмГТУ](https://vk.com/portalomgtu).", parse_mode="Markdown",disable_web_page_preview=True)
@router.message(F.text=='3')
async def message_answer(message: Message):
    await message.reply("Информацию о поддержке иностранных студентов, пересечении границ, стажировках, получении диплома европейского образца можно уточнить в отделе международных отношений ОмГТУ: interdepomgtu@gmail.com, 8 (3812) 65-64-92.", parse_mode="Markdown",disable_web_page_preview=True)
@router.message(F.text=='4')
async def message_answer(message: Message):
    await message.reply("С вопросами о жизни в общежитии помогут [заведующие секторами](https://vk.com/away.php?to=https%3A%2F%2Fwww.omgtu.ru%2Fentrant%2Finformation-about-the-hostels%2F&cc_key=).", parse_mode="Markdown",disable_web_page_preview=True)
@router.message(F.text=='5')
async def message_answer(message: Message):
    await message.reply("Оплатить обучение и общежитие можно с помощью онлайн-сервиса [на сайте вуза](https://vk.com/away.php?to=https%3A%2F%2Fomgtu.ru%2Fstudents%2Fpay%2F&cc_key=). Вопросы об оплате можно задать специалистам [отдела договорных отношений](https://vk.com/away.php?to=https%3A%2F%2Fomgtu.ru%2Fgeneral_information%2Fdepartments%2Fdepartment-of-the-contractual-relationship%2F&cc_key=).", parse_mode="Markdown",disable_web_page_preview=True)
@router.message(F.text=='6')
async def message_answer(message: Message):
    await message.reply("Стать частью творческого коллектива или записаться в спортивную секцию, получить поддержку студенческих инициатив можно, обратившись в отдел молодежной политики (главный корпус ОмГТУ, кабинет Г-221)."
                        "\nПолезная информация о различных конкурсах, форумах и других мероприятиях для обучающихся есть в группе Портала молодежных проектов и инициатив ОмГТУ.", parse_mode="Markdown",disable_web_page_preview=True)
@router.message(F.text=='7')
async def message_answer(message: Message):
    await message.reply("Получить консультацию квалифицированного медицинского работника можно в здравпункте в главном корпусе ОмГТУ, кабинет Г-212 или по телефону: 8 (3812) 65-99-18. Время работы: с 8.00 до 13.00, суббота и воскресенье – выходной.", parse_mode="Markdown",disable_web_page_preview=True)
@router.message(F.text=='8')
async def message_answer(message: Message):
    await message.reply("Получить учебную литературу, прочитать интересные книги, поиграть в настольные игры с друзьями можно, оформив читательский билет в [библиотеке ОмГТУ](https://vk.com/biblio_omgtu). Обслуживание читателей: в будние дни с 9:00 до 19:00, суббота – с 9:00 до 16:00, воскресенье – выходной.", parse_mode="Markdown",disable_web_page_preview=True)
@router.message(F.text=='9')
async def message_answer(message: Message):
    await message.reply("Информацию о работе в системах «Мираполис» (все формы обучения) и «Прометей» (очная, вечерняя формы бакалавриата/специалитета и магистратуры) можно получить, написав на почту технической поддержки: elearning@omgtu.tech или позвонив по номеру: 8 (3812) 65-31-80 (добавочный номер – 1)."
                        "\n«Прометей» (заочное обучение бакалавриат/специалитет): parol\\_prometey@mail.ru, 8 (3812) 65-33-94 (добавочный номер – 2)."
                        "\nПри обращении необходимо указать ФИО и группу.", parse_mode="Markdown",disable_web_page_preview=True)
@router.message(F.text=='10')
async def message_answer(message: Message):
    await message.reply("Также в вузе можно получить консультацию [психолога](https://vk.com/yaroslavbulynko) абсолютно бесплатно и анонимно.", parse_mode="Markdown",disable_web_page_preview=True)
@router.message(F.text=='11')
async def message_answer(message: Message):
    await message.reply("Представляет интересы студентов, организовывает мероприятия различной направленности, делает студенческую жизнь яркой и насыщенной [Объединенный совет обучающихся](https://vk.com/omgtuoso).", parse_mode="Markdown",disable_web_page_preview=True)
@router.message(F.text=='12')
async def message_answer(message: Message):
    await message.reply("Защитит права и окажет поддержку по различным вопросам [Первичная профсоюзная организация студентов ОмГТУ](https://vk.com/omgtuprof).", parse_mode="Markdown",disable_web_page_preview=True)

