-- Дана база данных произведений Шекспира,
--  в которой содержатся следующие 
-- таблицы: character - герои произведений,
--  work - произведения, chapter - главы произведений, paragraph - параграфы, wordform - слова, встречающиеся в произведениях
-- Напишите следующие запросы:
-- 1. Найдите 10 самых часто встречающихся слов.
-- 2. Найдите все слова, которые начинаются с буквы 'а', регистр не должен иметь значения.
-- 3. Найдите все произведения, которые относятся к жанру 'р'.
-- 4. Найдите среднее количество параграфов в произведения жанра t'.
-- 5. Выведите все произведения, в которых количество слов выше среднего.
-- 6. Выведите имя героя, количество его реплик, и произведение, в котором этот герой встречается.
-- 7. Выведите среднее количество реплик героев в произведении 'Romeo and Juliet'.
-- 8. Выведите общее количество слов в каждой из секций в таблице paragraph.
-- 9. Выведите всех героев, которые имеют от 15 до 30 реплик.
-- 10. Выведите все произведения, которые были написаны в 17 веке
-- 11. Найдите все произведения, которые имею в полном названии слово 'the'
-- 12. Выведите все уникальные секции в paragraph.
-- 13. Для каждой главы введите: id, описание и название прозведения, к которой относится
-- данная глава.
-- 14. Для каждого параграфа выведите: номер параграфа, имя героя, и количество реплик героя
-- -- 15. Для каждого параграфа выведите: номер параграфа, название произведения и год выхода этого произведения.

-- SELECT plaintext,occurences AS plaintext_count 
-- FROM wordform
-- LIMIT 10

-- to
-- 20136
-- of
-- 17169
-- a
-- 14943
-- you
-- 13989
-- my
-- 12950
-- in
-- 11512
-- that
-- 11487

-- 2 hw
-- SELECT plaintext
-- FROM wordform
-- WHERE plaintext LIKE '%a%'
-- LIMIT 200

-- 3 hw
-- SELECT title
-- FROM work
-- WHERE genretype like '%p%'



-- 4 hw
-- SELECT avg(totalparagraphs),w.genretype as paragraph_avg FROM paragraph p left JOIN work w
-- on p.workid = w.workid where w.genretype like '%t%' GROUP BY w.genretype
-- 1788.9437982850836234
-- t

-- 5 hw

-- SELECT title,totalwords
-- FROM work 
-- WHERE totalwords > (
--   SELECT avg(totalwords) 
--   FROM work
    -- -- )
    -- -- 	;
    -- title
    -- totalwords
    -- 1
    -- All's Well That Ends Well
    -- 22997
    -- 2
    -- Antony and Cleopatra
    -- 24905
    -- 3
    -- As You Like It
    -- 21690
    -- 4
    -- Coriolanus
    -- 27577
    -- 5
    -- Cymbeline

-- 6 hw
-- SELECT charname,speechcount FROM character GROUP BY charname,speechcount
-- Eleanor
-- 21
-- 93
-- Taurus
-- 1
-- 94
-- Marullus
-- 6
-- 95
-- Queen Elinor
-- 22
-- 96
-- Groom
-- 4
-- 97
-- Claudio
-- 125
-- 98
-- Dionyza
-- 19
-- 99
-- First Apparition
-- 1
-- 100
-- Casca
-- 39
-- 7 hw
-- SELECT avg(speechcount) FROM character 
-- join character_work cw on character.charid = cw.charid
-- JOIN work on work.workid = cw.workid
-- WHERE work.title LIKE 'Romeo and Juliet'

-- 8 hw
-- SELECT section,sum(wordcount)
-- FROM paragraph
-- GROUP BY section

-- 9 hw
-- SELECT charname,speechcount
-- FROM "character"
-- WHERE speechcount BETWEEN 15 and 30

-- 10hw
-- SELECT * from work WHERE year BETWEEN 1600 and 1700


-- 11 hw 
-- SELECT longtitle from work WHERE lower(longtitle) like '%the%'

-- 12 HW
-- SELECT DISTINCT section from paragraph

-- 13HW
-- SELECT ch.chapterid, ch.description, w.title
-- FROM chapter ch
-- JOIN work w ON ch.workid = w.workid;
-- 14 HW
-- SELECT p.paragraphnum, c.charname, c.speechcount
-- FROM paragraph p
-- JOIN "character" c ON p.charid = c.charid;
-- 15 hw
-- SELECT p.paragraphnum, w.title, w.year
-- FROM paragraph p
-- JOIN work w ON p.workid = w.workid;