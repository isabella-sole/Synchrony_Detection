%% Simple Spearman Rank Correlation Coefficient

x = transpose([velocity_MDRQA_results(1:91).recpercent]);
%y = table2array(SG_DVs(:,""));
y = [table2array(BR_DVs(:,"bayley_lang")); table2array(SG_DVs(:,"bayley_lang"))];
%x = [table2array(SG_DVs(:,"bayley_lang")); table2array(BR_DVs(:,"bayley_lang"))];
total_data = 91 - (sum(isnan(x)) + sum(isnan(y)) - sum(isnan(x).*isnan(y)))

p = polyfit(x,y,1);
f = polyval(p,x); 
plot(x,y,'.',x,f,'-','Color','Black','MarkerSize',24) 

ylabel('IBQ SUR') %your independent variable name
xlabel('MDRQA dyadic recurrence percent (neck-neck & nose-nose distance)') %your dependent variable name


[rho,pval] = corr(x,y, "type","Pearson","tail","both", "rows","complete");
disp("pval:") 
disp(pval) 
disp("rho:") 
disp(rho)

%% Try GLM2

temp_table_IV = struct2table(distance_MDRQA_results);
temp_table_DV = array2table([table2array(BR_DVs(:,"ibq_sur")); table2array(SG_DVs(:,"ibq_sur"))]);
% 
temp_table = [temp_table_IV(1:91,2:4), temp_table_DV(1:91,"Var1")];
disp("Result of bayley_lang")
%mdl_JSD = stepwiseglm(temp_table,"interactions","Dcistribution","normal");%,"ResponseVar","Material_shiftQ");
mdl_IBQ = fitglm(temp_table,"linear","Distribution","normal",Intercept=true);%,"ResponseVar","Material_shiftQ");
disp(mdl_IBQ.Coefficients)
disp(mdl_IBQ.Rsquared)

%% kruskal walis


KW_mat = [x,y]
[p_k, tbl_k, stats_k] = kruskalwallis(KW_mat, ["SG" "BR"],"on");