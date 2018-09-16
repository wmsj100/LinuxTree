# 计算行数

- select count(*) from pet; 获取pet表的总行数；
- select owner, count(*) from pet group by owner; 按照主人查询每个人拥有的宠物数量。
- select species, count(species) from pet group by species; 查询每种动物的数量；
- select species, sex, count(*) from pet group by species, sex; 按照种类和性别组合分类动物数量
- select species, sex, count(*) from pet where species='dog' or species='cat' group by species, sex; 只对猫狗进行查询
- select sex, count(*) from pet where sex like '_' group by sex;
- select sex, count(*) from pet where sex regexp 'f|g' group by sex;
