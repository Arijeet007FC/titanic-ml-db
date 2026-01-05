-- 1. Survival by class
SELECT pclass, 
       COUNT(*) as total, 
       SUM(survived) as survived,
       ROUND(AVG(survived)*100, 1) as survival_pct
FROM passengers 
WHERE survived IS NOT NULL 
GROUP BY pclass 
ORDER BY pclass;

-- 2. Survival by gender  
SELECT sex, 
       COUNT(*) as total, 
       SUM(survived) as survived,
       ROUND(AVG(survived)*100, 1) as survival_pct
FROM passengers 
WHERE survived IS NOT NULL 
GROUP BY sex;

-- 3. Age statistics
SELECT 
    ROUND(AVG(age),1) as avg_age,
    MIN(age) as youngest,
    MAX(age) as oldest,
    COUNT(*) as total_with_age
FROM passengers WHERE age IS NOT NULL;
