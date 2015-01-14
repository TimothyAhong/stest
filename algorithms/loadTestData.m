function [] = loadTestData()
close all
clear all
clc
    f_info = inputdlg({'Enter the date eg: nov_23','Enter if it was a short (s) or long (l) test:','Position (lying, sitting, standing):','Cap sensor left side(1-5):','Cap sensor right side(1-5):','Pressure sensor left side (1-4):','Pressure sensor left side (1-4):','Volume:'},...
               'Data processing for volume testing', [1 20; 1 20; 1 20; 1 20; 1 20; 1 20; 1 20; 1 20]);
           
    [date, test_length, pos, cl, cr, pl, pr, volm] = f_info{:};
    pathname = strcat('C:\Users\Danny\Desktop\Sensassure\data\test_',date,'\csv\');
    disp(pathname)
    
    capL = str2num(cl);
    capR = str2num(cr)+5;
    presL = str2num(pl)+10;
    presR = str2num(pr)+14;
    vol = str2num(volm);
    
    if(capL<1||capL>5||capR<5 ||capR>10||presL<10||presL>14||presR<14||presR>18)
        error('Left and Right cap sensor number must be between 1 and 5, inclusive. Left and Right pressure sesnor number must be between 1 and 4, inclusive. Volume must be multiple of 50, 0-400 and 600.');
    end
    
    n = 7;
    if(test_length ~= 's' || test_length ~= 'S')
        n = 10;
    end
    
    
    trans0to50 = load(fullfile(strcat(pathname, '0_50.csv')));
    trans50to100 = load(fullfile(strcat(pathname, '50_100.csv')));
    trans100to150 = load(fullfile(strcat(pathname, '100_150.csv')));
    trans150to200 = load(fullfile(strcat(pathname, '150_200.csv')));
    trans200to250 = load(fullfile(strcat(pathname, '200_250.csv')));
    trans250to300 = load(fullfile(strcat(pathname, '250_300.csv')));
    
    [t_r0_50, t__c0_50] = size(trans0to50);
    [t_r50_100, t__c50_100] = size(trans50to100);
    [t_r100_150, t__c100_150] = size(trans100to150);
    [t_r150_200, t__c150_200] = size(trans150to200);
    [t_r200_250, t__c200_250] = size(trans200to250);
    [t_r250_300, t__c250_300] = size(trans250to300);
    
    
    lying0 = load(fullfile(strcat(pathname,'0_lying.csv'))); 
    lying50 = load(fullfile(strcat(pathname,'50_lying.csv')));
    lying100 = load(fullfile(strcat(pathname,'100_lying.csv'))); 
    lying150 = load(fullfile(strcat(pathname,'150_lying.csv')));
    lying200 = load(fullfile(strcat(pathname,'200_lying.csv')));
    lying250 = load(fullfile(strcat(pathname,'250_lying.csv')));
    lying300 = load(fullfile(strcat(pathname,'300_lying.csv')));
    
    [l_r0, l_c0] = size(lying0);
    [l_r50, l_c50] = size(lying50);
    [l_r100, l_c100] = size(lying100);
    [l_r150, l_c150] = size(lying150);
    [l_r200, l_c200] = size(lying200);
    [l_r250, l_c250] = size(lying250);
    [l_r300, l_c300] = size(lying300);
    
    sitting0 = load(fullfile(strcat(pathname,'0_sitting.csv')));
    sitting50 = load(fullfile(strcat(pathname,'50_sitting.csv')));
    sitting100 = load(fullfile(strcat(pathname,'100_sitting.csv')));
    sitting150 = load(fullfile(strcat(pathname,'150_sitting.csv')));
    sitting200 = load(fullfile(strcat(pathname,'200_sitting.csv')));
    sitting250 = load(fullfile(strcat(pathname,'250_sitting.csv')));
    sitting300 = load(fullfile(strcat(pathname,'300_sitting.csv')));
    
    [si_r0, si_c0] = size(sitting0);
    [si_r50, si_c50] = size(sitting50);
    [si_r100, si_c100] = size(sitting100);
    [si_r150, si_c150] = size(sitting150);
    [si_r200, si_c200] = size(sitting200);
    [si_r250, si_c250] = size(sitting250);
    [si_r300, si_c300] = size(sitting300);
    
    standing0 = load(fullfile(strcat(pathname,'0_standing.csv')));
    standing50 = load(fullfile(strcat(pathname,'50_standing.csv')));
    standing100 = load(fullfile(strcat(pathname,'100_standing.csv'))); 
    standing150 = load(fullfile(strcat(pathname,'150_standing.csv')));
    standing200 = load(fullfile(strcat(pathname,'200_standing.csv')));
    standing250 = load(fullfile(strcat(pathname,'250_standing.csv')));
    standing300 = load(fullfile(strcat(pathname,'300_standing.csv')));
    
    [st_r0, st_c0] = size(standing0);
    [st_r50, st_c50] = size(standing50);
    [st_r100, st_c100] = size(standing100);
    [st_r150, st_c150] = size(standing150);
    [st_r200, st_c200] = size(standing200);
    [st_r250, st_c250] = size(standing250);
    [st_r300, st_c300] = size(standing300);
    
    
if(test_length ~= 's' && test_length ~= 'S')
    trans300to350 = load(fullfile(strcat(pathname, '300_350.csv')));
    trans350to400 = load(fullfile(strcat(pathname, '350_400.csv')));
    trans400to600 = load(fullfile(strcat(pathname, '400_600.csv')));
    
    [t_r300_350, t__c300_350] = size(trans300to350);
    [t_r350_400, t__c350_400] = size(trans350to400);
    [t_r400_600, t__c400_600] = size(trans400to600);
    
    lying350 = load(fullfile(strcat(pathname,'350_lying.csv')));
    lying400 = load(fullfile(strcat(pathname,'400_lying.csv')));
    lying600 = load(fullfile(strcat(pathname,'600_lying.csv')));
    
    [l_r350, l_c350] = size(lying350);
    [l_r400, l_c400] = size(lying400);
    [l_r600, l_c600] = size(lying600);    
    
    sitting350 = load(fullfile(strcat(pathname,'350_sitting.csv')));
    sitting400 = load(fullfile(strcat(pathname,'400_sitting.csv')));
    sitting600 = load(fullfile(strcat(pathname,'600_sitting.csv')));
    
    [si_r350, si_c350] = size(sitting350);
    [si_r400, si_c400] = size(sitting400);
    [si_r600, si_c600] = size(sitting600);    
    
    standing350 = load(fullfile(strcat(pathname,'350_standing.csv')));
    standing400 = load(fullfile(strcat(pathname,'400_standing.csv')));
    standing600 = load(fullfile(strcat(pathname,'600_standing.csv')));
    
    [st_r350, st_c350] = size(standing350);
    [st_r400, st_c400] = size(standing400);
    [st_r600, st_c600] = size(standing600);    
    
end


%-------------------------------------------lying------------------------------------
if(strcmp(pos, 'lying')==1)
    if(vol == 0)        
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(lying0(:,capL))
                subplot(2,1,2)            
                plot(lying0(:,presL))
            
            else
                plot(lying0(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(lying0(:,capR))
                subplot(2,1,2)
                plot(lying0(:,presR))
            else
                plot(lying0(:,capR))
            end
        end
        
    elseif(vol == 50)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(lying50(:,capL))
                subplot(2,1,2)            
                plot(lying50(:,presL))
            
            else
                plot(lying50(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(lying50(:,capR))
                subplot(2,1,2)
                plot(lying50(:,presR))
            else
                plot(lying50(:,capR))
            end
        end
        
    elseif(vol == 100)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(lying100(:,capL))
                subplot(2,1,2)            
                plot(lying100(:,presL))
            
            else
                plot(lying100(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(lying100(:,capR))
                subplot(2,1,2)
                plot(lying100(:,presR))
            else
                plot(lying100(:,capR))
            end
        end
        
    elseif(vol == 150)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(lying150(:,capL))
                subplot(2,1,2)            
                plot(lying150(:,presL))
            
            else
                plot(lying150(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(lying150(:,capR))
                subplot(2,1,2)
                plot(lying150(:,presR))
            else
                plot(lying150(:,capR))
            end
        end
        
    elseif(vol == 200)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(lying200(:,capL))
                subplot(2,1,2)            
                plot(lying200(:,presL))
            
            else
                plot(lying200(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(lying200(:,capR))
                subplot(2,1,2)
                plot(lying200(:,presR))
            else
                plot(lying200(:,capR))
            end
        end
        
    elseif(vol == 250)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(lying250(:,capL))
                subplot(2,1,2)            
                plot(lying250(:,presL))
            
            else
                plot(lying250(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(lying250(:,capR))
                subplot(2,1,2)
                plot(lying250(:,presR))
            else
                plot(lying250(:,capR))
            end
        end
        
    elseif(vol == 300)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(lying300(:,capL))
                subplot(2,1,2)            
                plot(lying300(:,presL))
            
            else
                plot(lying300(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(lying300(:,capR))
                subplot(2,1,2)
                plot(lying300(:,presR))
            else
                plot(lying300(:,capR))
            end
        end
        
    elseif(vol == 350)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(lying350(:,capL))
                subplot(2,1,2)            
                plot(lying350(:,presL))
            
            else
                plot(lying350(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(lying350(:,capR))
                subplot(2,1,2)
                plot(lying350(:,presR))
            else
                plot(lying350(:,capR))
            end
        end
       
    elseif(vol == 400)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(lying400(:,capL))
                subplot(2,1,2)            
                plot(lying400(:,presL))
            
            else
                plot(lying400(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(lying400(:,capR))
                subplot(2,1,2)
                plot(lying400(:,presR))
            else
                plot(lying400(:,capR))
            end
        end
       
    elseif(vol == 600)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(lying600(:,capL))
                subplot(2,1,2)            
                plot(lying600(:,presL))
            
            else
                plot(lying600(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(lying600(:,capR))
                subplot(2,1,2)
                plot(lying600(:,presR))
            else
                plot(lying600(:,capR))
            end
        end
        
    end
%-------------------------------------------sitting------------------------------------    
elseif(strcmp(pos, 'sitting') == 1)
   if(vol == 0)        
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(sitting0(:,capL))
                subplot(2,1,2)            
                plot(sitting0(:,presL))
            
            else
                plot(sitting0(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(sitting0(:,capR))
                subplot(2,1,2)
                plot(sitting0(:,presR))
            else
                plot(sitting0(:,capR))
            end
        end
        
    elseif(vol == 50)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(sitting50(:,capL))
                subplot(2,1,2)            
                plot(sitting50(:,presL))
            
            else
                plot(sitting50(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(sitting50(:,capR))
                subplot(2,1,2)
                plot(sitting50(:,presR))
            else
                plot(sitting50(:,capR))
            end
        end
        
    elseif(vol == 100)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(sitting100(:,capL))
                subplot(2,1,2)            
                plot(sitting100(:,presL))
            
            else
                plot(sitting100(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(sitting100(:,capR))
                subplot(2,1,2)
                plot(sitting100(:,presR))
            else
                plot(sitting100(:,capR))
            end
        end
        
    elseif(vol == 150)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(sitting150(:,capL))
                subplot(2,1,2)            
                plot(sitting150(:,presL))
            
            else
                plot(sitting150(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(sitting150(:,capR))
                subplot(2,1,2)
                plot(sitting150(:,presR))
            else
                plot(sitting150(:,capR))
            end
        end
        
    elseif(vol == 200)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(sitting200(:,capL))
                subplot(2,1,2)            
                plot(sitting200(:,presL))
            
            else
                plot(sitting200(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(sitting200(:,capR))
                subplot(2,1,2)
                plot(sitting200(:,presR))
            else
                plot(sitting200(:,capR))
            end
        end
        
    elseif(vol == 250)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(sitting250(:,capL))
                subplot(2,1,2)            
                plot(sitting250(:,presL))
            
            else
                plot(sitting250(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(sitting250(:,capR))
                subplot(2,1,2)
                plot(sitting250(:,presR))
            else
                plot(sitting250(:,capR))
            end
        end
        
    elseif(vol == 300)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(sitting300(:,capL))
                subplot(2,1,2)            
                plot(sitting300(:,presL))
            
            else
                plot(sitting300(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(sitting300(:,capR))
                subplot(2,1,2)
                plot(sitting300(:,presR))
            else
                plot(sitting300(:,capR))
            end
        end
        
    elseif(vol == 350)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(sitting350(:,capL))
                subplot(2,1,2)            
                plot(sitting350(:,presL))
            
            else
                plot(sitting350(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(sitting350(:,capR))
                subplot(2,1,2)
                plot(sitting350(:,presR))
            else
                plot(sitting350(:,capR))
            end
        end
       
    elseif(vol == 400)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(sitting400(:,capL))
                subplot(2,1,2)            
                plot(sitting400(:,presL))
            
            else
                plot(sitting400(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(sitting400(:,capR))
                subplot(2,1,2)
                plot(sitting400(:,presR))
            else
                plot(sitting400(:,capR))
            end
        end
       
    elseif(vol == 600)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(sitting600(:,capL))
                subplot(2,1,2)            
                plot(sitting600(:,presL))
            
            else
                plot(sitting600(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(sitting600(:,capR))
                subplot(2,1,2)
                plot(sitting600(:,presR))
            else
                plot(sitting600(:,capR))
            end
        end
        
    end
    
%-------------------------------------------standing------------------------------------
elseif(strcmp(pos, 'standing') == 1)
    if(vol == 0)        
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(standing0(:,capL))
                subplot(2,1,2)            
                plot(standing0(:,presL))
            
            else
                plot(standing0(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(standing0(:,capR))
                subplot(2,1,2)
                plot(standing0(:,presR))
            else
                plot(standing0(:,capR))
            end
        end
        
    elseif(vol == 50)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(standing50(:,capL))
                subplot(2,1,2)            
                plot(standing50(:,presL))
            
            else
                plot(standing50(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(standing50(:,capR))
                subplot(2,1,2)
                plot(standing50(:,presR))
            else
                plot(standing50(:,capR))
            end
        end
        
    elseif(vol == 100)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(standing100(:,capL))
                subplot(2,1,2)            
                plot(standing100(:,presL))
            
            else
                plot(standing100(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(standing100(:,capR))
                subplot(2,1,2)
                plot(standing100(:,presR))
            else
                plot(standing100(:,capR))
            end
        end
        
    elseif(vol == 150)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(standing150(:,capL))
                subplot(2,1,2)            
                plot(standing150(:,presL))
            
            else
                plot(standing150(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(standing150(:,capR))
                subplot(2,1,2)
                plot(standing150(:,presR))
            else
                plot(standing150(:,capR))
            end
        end
        
    elseif(vol == 200)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(standing200(:,capL))
                subplot(2,1,2)            
                plot(standing200(:,presL))
            
            else
                plot(standing200(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(standing200(:,capR))
                subplot(2,1,2)
                plot(standing200(:,presR))
            else
                plot(standing200(:,capR))
            end
        end
        
    elseif(vol == 250)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(standing250(:,capL))
                subplot(2,1,2)            
                plot(standing250(:,presL))
            
            else
                plot(standing250(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(standing250(:,capR))
                subplot(2,1,2)
                plot(standing250(:,presR))
            else
                plot(standing250(:,capR))
            end
        end
        
    elseif(vol == 300)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(standing300(:,capL))
                subplot(2,1,2)            
                plot(standing300(:,presL))
            
            else
                plot(standing300(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(standing300(:,capR))
                subplot(2,1,2)
                plot(standing300(:,presR))
            else
                plot(standing300(:,capR))
            end
        end
        
    elseif(vol == 350)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(standing350(:,capL))
                subplot(2,1,2)            
                plot(standing350(:,presL))
            
            else
                plot(standing350(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(standing350(:,capR))
                subplot(2,1,2)
                plot(standing350(:,presR))
            else
                plot(standing350(:,capR))
            end
        end
       
    elseif(vol == 400)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(standing400(:,capL))
                subplot(2,1,2)            
                plot(standing400(:,presL))
            
            else
                plot(standing400(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(standing400(:,capR))
                subplot(2,1,2)
                plot(standing400(:,presR))
            else
                plot(standing400(:,capR))
            end
        end
       
    elseif(vol == 600)
        if(capL >0 && capL<6)
            figure
            if( presL > 10 && presL<15)                
                subplot(2,1,1)
                plot(standing600(:,capL))
                subplot(2,1,2)            
                plot(standing600(:,presL))
            
            else
                plot(standing600(:,capL))
            end
        end
        
        if(capR>5 && capR<11)
            figure
            if(presR > 14 && presR <19)
                subplot(2,1,1)
                plot(standing600(:,capR))
                subplot(2,1,2)
                plot(standing600(:,presR))
            else
                plot(standing600(:,capR))
            end
        end
        
    end
    
end









    



