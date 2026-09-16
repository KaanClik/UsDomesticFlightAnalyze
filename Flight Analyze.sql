--data
select * from FlightAnalyze..AverageFares$

delete from FlightAnalyze..AverageFares$ where Airport_Code is null;

--state analysis
select  State_Name, round(avg(Average_fare),2) as avg_fare_by_state, round(min(average_fare),2) as mýn_avg_by_state, 
round(max(average_fare),2) as max_avg_by_state,
round(STDEV(average_fare),2) as stdev_by_state, count(*) as total_ap_count, SUM(Passengers_Sample10) as total_sample_by_state
from FlightAnalyze..AverageFares$
group by State_Name 
order by avg_fare_by_state desc;



--in state ranking
select State_Name, Airport_Code,Airport_Name,round(Average_Fare,2) as avg_fare, rank() over (partition by State_Name order by [Average_Fare] desc) 
as rank_in_state 
from FlightAnalyze..AverageFares$
where Airport_Code is not null
order by State_Name, rank_in_state;

select Top(10) State_Name, avg(Average_fare) as avg_by_state,avg(Inflation_Adjusted_Average_Fare_Q1_2026) as avg_inf, min(average_fare) as mýn_avg_by_state, max(average_fare) max_avg_by_state,
STDEV(average_fare) as stdev_by_state, count(*) as total_ap_count, SUM(Passengers_Sample10) as total_sample_by_state,
avg(Average_fare) - avg(Inflation_Adjusted_Average_Fare_Q1_2026) as fare_diff,
(avg(Average_fare) - avg(Inflation_Adjusted_Average_Fare_Q1_2026))/avg(Inflation_Adjusted_Average_Fare_Q1_2026) as pct_change
from FlightAnalyze..AverageFares$
group by State_Name 
order by pct_change desc;


--volume

WITH VolumeTiers AS (
    SELECT 
        Airport_Code,
        Airport_Name,
        State_Name,
        Average_Fare,
        Passengers_Sample10,
        NTILE(3) OVER (ORDER BY Passengers_Sample10 DESC) AS volume_tier
    FROM FlightAnalyze..AverageFares$
    WHERE Airport_Code IS NOT NULL
)
SELECT 
    volume_tier,
    CASE 
        WHEN volume_tier = 1 THEN 'High Volume '
        WHEN volume_tier = 2 THEN 'Mid Volume'
        WHEN volume_tier = 3 THEN 'Low Volume'
    END AS tier_exp,
    COUNT(*) AS ap_count,
    ROUND(AVG(Average_Fare), 2) AS avg_ticket_price,
    MIN(Passengers_Sample10) AS min_passenger,
    MAX(Passengers_Sample10) AS max_passenger
FROM VolumeTiers
GROUP BY volume_tier
ORDER BY volume_tier ASC;
 
 --for bý and python to correlation 
 select Airport_Code, Airport_Name,City_Name,State_Name, Passengers_Sample10,round( Average_Fare,2) as avg_fare from FlightAnalyze..AverageFares$
 order by Passengers_Sample10

 --for bý most expensive 5 and cheapest 5 airports
SELECT * FROM (
    SELECT TOP(5)  Airport_Code, Airport_Name, Average_Fare, 
        'Cheapest 5' AS Category  
    FROM FlightAnalyze..AverageFares$
    ORDER BY Average_Fare ASC
) AS Ucuzlar
UNION ALL
SELECT * FROM (
    SELECT TOP(5) Airport_Code, Airport_Name, Average_Fare, 
        'Most Expensive 5' AS Category 
    FROM FlightAnalyze..AverageFares$
    ORDER BY Average_Fare DESC
) AS Pahalilar
ORDER BY Average_Fare DESC;

--for bý inside city competetion

select City_Name, count(airport_code) as Airport_count, round(avg(Average_Fare),2) as city_avg_price from FlightAnalyze..AverageFares$
group by city_name
having count(airport_code) >1
order by Airport_count desc;	

--for bý percentage of sample 

select Airport_Code, Passengers_Sample10, round(Passengers_Sample10 * 100.0/sum(Passengers_Sample10) over(),2) as perc_of_sample from FlightAnalyze..AverageFares$
where Passengers_Sample10 is not null 
order by perc_of_sample desc;


	   
	   
