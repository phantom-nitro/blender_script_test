import bpy
import random

row, col = 10, 10
spacing = 2
materi = ["Material.003", "Material.004", "Material.005", "Material.007", "Material.008"]

for i in range(-row, row):
    for j in range(-col, col): 
        
        item = bpy.context.object
            
               
        location=(i * spacing, j * spacing, random.random())
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location = location, scale=(1, 1, 1))
        # base color
        item.data.materials.append(bpy.data.materials["Material.001"])
        #height = int(random.random()*2)
        value = random.random()
        if value>0.8:
            height = random.randint(1, 2)
        else:
            height = 0
        
        for k in range(height):
            bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location = (i * spacing, j * spacing, (k+1) * spacing), scale=(1, 1, 1))
            item2 = bpy.context.object
            
            if random.random() < 0.2:
                choose = random.randint(0, 4)
                mat = materi[choose]
                item2.data.materials.append(bpy.data.materials[mat])
            else:
                item2.data.materials.append(bpy.data.materials["Material.001"])
            
            '''if k == 4:
                item2.data.materials.append(bpy.data.materials["Material.003"])
            if k == 3:
                item2.data.materials.append(bpy.data.materials["Material.006"])
            if k == 2:
                item2.data.materials.append(bpy.data.materials["Material.005"])
            if k == 1:
                item2.data.materials.append(bpy.data.materials["Material.007"])
            if k == 0:
                item2.data.materials.append(bpy.data.materials["Material.008"])
                
            if random.random() < 0.1:
                item2.data.materials.append(bpy.data.materials["Material.003"])'''
            '''else:
                item2.data.materials.append(bpy.data.materials["Material.001"])'''
