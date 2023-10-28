CREATE TABLE appleStore_description_combined AS

SELECT * FROM appleStore_description1

UNION ALL

SELECT * FROM appleStore_description2

UNION ALL

SELECT * FROM appleStore_description3

UNION ALL

SELECT * FROM appleStore_description4


--Exploratory Data Analysis--

-- checking the number of unique apps in both tablesAppleStore

SELECT COUNT(DISTINCT id) AS UniqueAppIDs
FROM AppleStore -- =7197

SELECT COUNT(DISTINCT id) AS UniqueAppIDs
FROM appleStore_description_combined -- =7197

--checking for any missing values 

SELECT COUNT(*) as MissingValues
from AppleStore
where track_name is null or user_rating is null or prime_genre is NULL -- =0

SELECT COUNT(*) as MissingValues
from appleStore_description_combined
where app_desc is null -- =0

--Finding out the number of apps per genre

SELECT prime_genre, COUNT(*) as NumApps
FROM AppleStore
group by prime_genre
order by NumApps DESC -- = games(3862), Entertainment(535), Education(453), Photos&Video(349), Utiilties(248), Health&Fitness(180), Productivity(178), Social Networking(167), Lifestyle(144), Music(138), Shopping(122), Sports(114), Books(112), Finance(104),
					  --   Travel(81), News(75), Wheather(72), Reference(64), Food&Drink(63), Business(57), Navigation(46), Medical(23), Catalogs(10)   DOUBLE CHECK NUMS AND SPELLING ARE CORRECT BEFORE PLOTING 

---overview of the apps ratings 

SELECT min(user_rating) as MinRating,
	   max(user_rating) AS MaxRating,
       avg(user_rating) AS AvgRating
FROM AppleStore -- = MinRating(0), MaxRating(5), AvgRating(3.5)

--Determining whether paid apps have higher ratings than free apps 

SELECT CASE 
			when price > 0 THEN 'paid'
            ELSe 'free'
		END AS App_Type ,
        avg(user_rating) as Avg_Rating
from AppleStore
group by App_Type --  Avg ratings paid apps(3.7) ,   Avg ratings free apps(3.37)

--checking if apps with more supported languages have higher ratings

select case
			WHEN lang_num < 10 THEN '<10 languages'
            when lang_num BETWEEN 10 and 30 then '10-30 languages'
            ELSE '>30 languages'
		end as language_bucket,
        avg(user_rating) as Avg_Rating
FROM AppleStore
GROUP BY language_bucket
ORDER by Avg_Rating desc -- Avg ratings apps with 10-30 languages(4.1) ,  Avg ratings apps with >30 languages(3.7) ,  Avg ratings apps with <10  languages(3.7)


--checking genre with low ratings 

SELECT prime_genre,
		avg(user_rating) as Avg_Rating
FROM AppleStore
group by prime_genre
order by Avg_rating asc 
LIMIT 24                                                                --(listing all genre by theyre avg rating from low to high)

-- Catalogs(2.1) , Finance(2.43), Books(2.47), Navigation(2.68), Lifestyle(2.8), News(2.98), Sports(2.982),  Social Networking(2.985), Food&Drink(3.18),  Entertainment(3.23),  Utiilties(3.278), Medical(3.369), Education(3.37)
-- Travel(3.37), Reference(3.45), Shopping(3.54), Weather(3.59), Games(3.68), Health&Fitness(3.7), Business(3.74), Photo&Video(3.8), Music(3.97), Productivity(4.0) DOUBLE CHECK NUMS AND SPELLING ARE CORRECT BEFORE PLOTING 

--checking if there is a relation between length of the app description and the user rating

SELECT case
			when length(b.app_desc) <500 then 'Short'
            when length(b.app_desc) BETWEEN 500 and 1000 then 'Medium'
            ELSE 'long'
        end as description_length_bucket,
        avg(a.user_rating) as average_rating 
            
from
	AppleStore aS A 
JOIN
	appleStore_description_combined AS b
on
	a.id = b.id 

group by description_length_bucket
order by average_rating  desc -- Long app description avg rating(3.85) , Medium app description avg rating(3.23), Short app description avg rating(2.53)

--checking the top_rated apps for each genre

select 
	prime_genre,
    track_name,
    user_rating
from (
		SELECT
		prime_genre,
		track_name,
		user_rating,
		RANK() OVER (PARTITION BY prime_genre order by user_rating desc , rating_count_tot desc) as rank
        FROM
        AppleStore
       ) as a 
 where
 a.rank = 1
        -- BOOK = "Color Therapy Adult Coloring Book for Adults"(5) , Business = "TurboScan™ Pro - document & receipt scanner: scan multiple pages and photos to PDF"(5), Catalogs = "CPlus for Craigslist app - mobile classifieds"(5)
        -- Education = "Elevate - Brain Training and Games"(5) , Entertainment = "Bruh-Button", Finance = "Credit Karma: Free Credit Scores, Reports & Alerts"(5), Food&Drink = "Domino's Pizza USA"(5)
        -- Games = "Head Soccer"(5), Health&Fitness = "Yoga Studio"(5), Lifestyle = "ipsy - Makeup, subscription and beauty tips"(5), Medical = "Blink Health"(5), Music = "Tenuto"(5), 
        -- Navigation = "parkOmator – for Apple Watch meter expiration timer, notifications & GPS navigator to car location"(5), News = "The Guardian"(5), Photo&Video = "Pic Collage - Picture Editor & Photo Collage Maker"
        --Productivity = "VPN Proxy Master - Unlimited WiFi security VPN"(5), Reference = "Sky Guide: View Stars Night or Day"(5), Shopping = "Zappos: shop shoes & clothes, fast free shipping"(5),
        --Social Networking = "We Heart It - Fashion, wallpapers, quotes, tattoos", Sports = "J23 - Jordan Release Dates and History"(5), Travel = "Urlaubspiraten"(5), Utilities ="Flashlight Ⓞ"(5),
        --Weather = "NOAA Hi-Def Radar Pro -  Storm Warnings, Hurricane Tracker & Weather Forecast"(5)
        --DOUBLE CHECK NUMS AND SPELLING ARE CORRECT BEFORE PLOTING 
