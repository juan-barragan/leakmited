# import shapefile
# import matplotlib.pyplot as plt

# sf = shapefile.Reader("regions-20180101-shp/regions-20180101.shp")
# shapes = sf.shapes()
# print len(shapes)
# plt.figure()
# for shape in sf.shapeRecords():
#     x = [i[0] for i in shape.shape.points[:]]
#     y = [i[1] for i in shape.shape.points[:]]
#     plt.plot(x,y)
# plt.show()


from descartes import PolygonPatch
import shapefile
import matplotlib.pyplot as plt


sf=shapefile.Reader('departements-20180101-shp/departements-20180101.shp')
fig = plt.figure() 
ax = fig.gca()  
for poly in sf.shapes():
    poly_geo=poly.__geo_interface__

    ax.add_patch(PolygonPatch(poly_geo, fc='#ffffff', ec='#FF0000', alpha=0.5, zorder=2 ))
     
poly_geo =      {
         "type": "Polygon",
         "coordinates": [[
             [-0.198840174520842, 43.70794322452202], [-0.222235915236875, 43.71887029533192], [-0.19414330237234, 43.737016685694684], [-0.180792917516703, 43.73392241336569], [-0.166464609500636, 43.74073425722042], [-0.158609760122906, 43.733001456816694], [-0.165604514951094, 43.72182035935971], [-0.17757883861499, 43.71205146251945], [-0.198840174520842, 43.70794322452202]]]
     }
# poly_geo = [[-0.198840174520842, 43.70794322452202], [-0.222235915236875, 43.71887029533192], [-0.19414330237234, 43.737016685694684], [-0.180792917516703, 43.73392241336569], [-0.166464609500636, 43.74073425722042], [-0.158609760122906, 43.733001456816694], [-0.165604514951094, 43.72182035935971], [-0.17757883861499, 43.71205146251945], [-0.198840174520842, 43.70794322452202]]
ax.add_patch(PolygonPatch(poly_geo, fc='#0000ff', ec='#FF0000', alpha=0.5, zorder=2 ))
ax.axis('scaled')
plt.show()