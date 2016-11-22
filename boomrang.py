import math
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            pdist = {}
            for j in range(len(points)):
                val =  (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                if val in pdist:
                    pdist[val] += 1
                else:
                    pdist[val] = 1
            for val in pdist:
                res += pdist[val] *(pdist[val] - 1)
        return res

digit = [[693,334],[439,334],[421,159],[985,957],[354,761],[762,972],[541,716],[852,850],[662,482],[399,217],[154,173],[15,506],[851,364],[790,263],[491,172],[37,537],[859,828],[871,280],[987,856],[590,341],[970,352],[665,511],[69,517],[361,83],[351,112],[300,506],[638,667],[364,489],[32,154],[104,875],[679,141],[412,538],[969,636],[170,956],[844,760],[649,814],[465,314],[326,886],[183,39],[969,535],[152,621],[393,790],[289,109],[631,673],[264,735],[548,295],[877,313],[833,198],[949,355],[155,793],[468,156],[960,933],[823,286],[171,358],[677,140],[245,181],[761,990],[323,50],[100,954],[75,364],[42,624],[659,919],[289,844],[469,238],[551,976],[383,19],[133,343],[304,956],[981,475],[666,11],[967,912],[192,729],[902,868],[131,2],[174,207],[718,216],[183,377],[487,472],[573,957],[62,125],[933,797],[496,418],[141,153],[726,474],[980,393],[485,948],[305,30],[29,559],[898,160],[562,424],[719,280],[641,902],[10,480],[726,583],[789,140],[708,723],[938,557],[493,431],[710,220],[905,690],[613,391],[638,270],[421,667],[829,671],[180,743],[95,899],[24,88],[154,386],[569,232],[969,710],[373,30],[433,663],[587,279],[94,649],[499,351],[339,464],[742,330],[86,515],[349,915],[186,881],[11,634],[133,387],[722,287],[773,643],[519,742],[354,244],[124,139],[259,63],[418,353],[712,269],[705,404],[733,799],[734,819],[315,435],[87,853],[669,450],[487,802],[837,562],[89,610],[205,960],[704,911],[557,829],[403,816],[892,821],[522,605],[443,579],[361,528],[378,447],[700,45],[882,787],[899,551],[589,386],[353,426],[948,794],[36,506],[107,92],[417,664],[921,820],[480,166],[994,354],[123,437],[933,484],[317,312],[931,17],[709,165],[156,608],[69,745],[995,422],[171,295],[569,559],[801,676],[652,571],[340,925],[743,172],[91,89],[527,566],[878,812],[50,196],[124,333],[213,186],[499,370],[794,568],[115,141],[342,639],[437,263],[198,590],[939,202],[513,631],[128,257],[804,571],[346,683],[138,225],[495,540],[421,972],[226,634],[158,725],[356,952],[645,472],[446,339],[111,883],[603,661],[825,542],[216,339],[174,344],[596,330],[267,294],[13,757],[519,860],[650,292],[832,876],[279,990],[953,635],[295,598],[107,741],[937,570],[976,540],[584,801],[83,800],[492,609],[496,440],[939,763],[735,304],[873,606],[164,523],[251,349],[751,530],[339,704],[165,986],[302,625],[79,591],[547,407],[484,131],[561,919],[931,53],[528,427],[494,819],[543,581],[123,768],[187,639],[643,438],[988,394],[320,680],[98,486],[18,752],[463,98],[695,10],[505,179],[142,66],[98,425],[472,978],[853,966],[797,748],[547,272],[516,86],[912,159],[877,900],[553,197],[932,3],[35,951],[107,498],[49,154],[861,906],[334,3],[325,784],[428,797],[763,633],[115,560],[381,14],[185,897],[100,97],[408,329],[349,313],[879,634],[316,914],[585,775],[765,986],[930,626],[892,616],[629,569],[752,409],[366,515],[395,833],[428,776],[847,613],[26,300],[62,786],[629,763],[100,508],[397,416],[775,982],[544,540],[320,826],[518,565],[794,499],[134,546],[908,853],[62,303],[686,842],[432,534],[807,810],[834,869],[596,815],[984,696],[324,382],[465,451],[716,361],[343,37],[187,861],[602,981],[360,88],[879,620],[941,293],[924,628],[135,708],[162,942],[870,996],[163,466],[811,500],[515,487],[234,332],[290,950],[693,633],[339,880],[494,293],[213,854],[382,444],[475,323],[738,751],[951,873],[811,465],[168,681],[813,683],[499,977],[535,14],[464,769],[346,107],[72,391],[740,411],[623,587],[57,836],[793,439],[281,620],[114,371],[371,418],[596,534],[883,764],[567,697],[800,67],[674,335],[433,490],[457,132],[949,529],[523,690],[292,147],[629,349],[335,422],[140,968],[43,255],[339,766],[25,936],[653,260],[52,220],[957,204],[287,983],[540,721],[826,997],[205,127],[878,728],[169,170],[227,798],[520,563],[221,660],[883,616],[267,223],[382,292],[511,35],[553,563],[608,862],[768,895],[198,660],[968,376],[9,173],[503,887],[254,673],[57,481],[823,929],[396,44],[942,280],[12,209],[855,747],[854,366],[134,759],[281,742],[973,401],[638,171],[413,958],[899,422],[484,755],[661,90],[780,71],[923,603],[0,320],[0,942],[952,12],[504,807],[759,358],[525,894],[117,158],[636,90],[560,626],[614,973],[937,865],[748,421],[620,409],[863,400],[832,786],[4,833],[458,356],[127,410],[368,631],[569,128],[341,446],[374,458],[605,10],[901,165],[989,867],[490,926],[732,238],[699,705],[0,562],[457,832],[348,461],[17,807],[169,497],[569,538],[128,139],[18,470],[585,392],[280,542],[754,533],[707,743],[400,550],[21,485],[788,720],[190,140],[634,647],[325,983],[461,694],[142,630],[191,63],[520,320],[554,538],[142,492],[930,422],[34,685],[308,94],[780,708],[644,802],[545,784],[522,87],[925,157],[735,602],[492,548],[296,986],[530,840],[49,51],[512,956],[589,654],[448,872],[428,482],[557,88],[576,337],[797,220],[139,694],[5,14],[782,282],[523,869],[236,15],[417,884],[353,299],[724,754],[350,236],[710,292],[242,158],[164,23],[641,721],[111,569],[410,260],[790,902],[955,147],[916,89],[781,439],[958,17],[806,375],[901,511],[674,978],[265,377],[566,976],[669,161],[134,833]]

m = Solution()
print m.numberOfBoomerangs(digit)