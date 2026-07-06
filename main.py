from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Configuração do banco SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#Criando a tabela que vai interligar a tabela cor com a tabela de paletas
paleta_cor = db.Table(
    "paleta_cor",
    db.Column("id_paleta", db.Integer, db.ForeignKey("Paletas.id_paleta"), primary_key=True),
    db.Column("id_cor", db.Integer, db.ForeignKey("Cores.id_cor"), primary_key=True)
)


class Cor(db.Model):
    __tablename__ = "Cores"

    id_cor = db.Column(db.Integer, primary_key=True)
    nome_cor = db.Column(db.String(100), nullable=False)
    hex = db.Column(db.String(7), nullable=False, unique=True)

    paletas = db.relationship(
        "Paleta",
        secondary=paleta_cor,
        back_populates="cores"
    )

class Paleta(db.Model):
    __tablename__ = "Paletas"

    id_paleta = db.Column(db.Integer, primary_key=True)
    nome_cor_paleta = db.Column(db.String(100), nullable=False)

    cores = db.relationship(
        "Cor",
        secondary=paleta_cor,
        back_populates="paletas"
    )


#Criando o modelo do banco de dados
with app.app_context():
    db.create_all()
       

@app.route("/inserir_cores")
def inserir_cores():
    if Cor.query.first():
        return "Banco já possui cores."

    cores = [
        #preto (tudo ok)
        Cor(nome_cor="Preto", hex="#000000"),
        Cor(nome_cor="Riele black", hex="#030206"),
        Cor(nome_cor="Blackout", hex="#0C0A03"),
        Cor(nome_cor="Smoky black", hex="#11100D"),
        Cor(nome_cor="Licorice", hex="#1E0D0A"),
        Cor(nome_cor="Black cherry", hex="#28171D"),
        Cor(nome_cor="Pantone Black C", hex="#2D2926"),
        #Cinza (tudo ok)
        Cor(nome_cor="Dim gray", hex="#696969"),
        Cor(nome_cor="Pantone Cool Gray 11 C", hex="#53565A"),
        Cor(nome_cor="Aluminium", hex="#7F858B"),
        Cor(nome_cor="Pantone Warm Gray 11 C", hex="#6E6259"),
        Cor(nome_cor="teakwood", hex="#8C7A6C"),
        Cor(nome_cor="Dark grayish blue", hex="#9CA3AF"),
        Cor(nome_cor="Sofi taupe", hex="#A39384"),
        Cor(nome_cor="Reindeer", hex="#B7A596"),
        Cor(nome_cor="Navajo white 3", hex="#CDB38B"),
        Cor(nome_cor="Azure 4", hex="#838B8B"),
        Cor(nome_cor="Cinza", hex="#808080"),
        Cor(nome_cor="Cinza escuro claro", hex="#A9A9A9"),
        Cor(nome_cor="Cinza escuro azulado", hex="#2F4F4F"),
        Cor(nome_cor="Ardósia cinza", hex="#708090"),
        Cor(nome_cor="Seashell 4", hex="#8B8682"),
        Cor(nome_cor="Old silver", hex="#7f858b"),
        Cor(nome_cor="Dolpin gray", hex="#828d85"),
        Cor(nome_cor="Cinza claro", hex="#778899"),
        Cor(nome_cor="Azure 3", hex="#C1CDCD"),
        Cor(nome_cor="Prata", hex="#C0C0C0"),
        Cor(nome_cor="Azure 2", hex="#E0EEEE"),
        Cor(nome_cor="Pantone 670 C", hex="#E7D6E8"),
        Cor(nome_cor="Seashell 3", hex="#CDC5BF"),
        Cor(nome_cor="Seashell 2", hex="#EEE5DE"),
        Cor(nome_cor="Seashell", hex="#FFF5EE"),
        #Branco (Tudo ok)
        Cor(nome_cor="Cloud", hex="#CDD0DB"),
        Cor(nome_cor="Dark vanilla", hex="#C5C0AA"),
        Cor(nome_cor="Gainsboro", hex="#DCDCDC"),
        Cor(nome_cor="Silver wisteria", hex="#DAD4D7"),
        Cor(nome_cor="Cinza clarinho", hex="#D3D3D3"),
        Cor(nome_cor="Branco", hex="#FFFFFF"),
        Cor(nome_cor="Bege", hex="#F5F5DC"),
        Cor(nome_cor="Fumaça branca", hex="#F5F5F5"),
        Cor(nome_cor="Beige", hex="#F7FAD5"),
        Cor(nome_cor="Meringe", hex="#E8EBED"),
        Cor(nome_cor="Unem cream", hex="#E4DFD3"),
        Cor(nome_cor="Branco antigo", hex="#FAEBD7"),
        Cor(nome_cor="Seda de milho", hex="#FFF8DC"),
        Cor(nome_cor="Light goldenrod", hex="#FAFAD2"),
        Cor(nome_cor="Luz amarela", hex="#FFFFE0"),
        Cor(nome_cor="Linho", hex="#FAF0E6"),
        Cor(nome_cor="Renda velha", hex="#FDF5E6"),
        Cor(nome_cor="Branco floral", hex="#FFFAF0"),
        Cor(nome_cor="Fantasma branco", hex="#F8F8FF"),
        Cor(nome_cor="Alice Blue", hex="#F0F8FF"),
        Cor(nome_cor="Lavanda", hex="#E6E6FA"),
        Cor(nome_cor="Melada", hex="#F0FFF0"),
        Cor(nome_cor="Marfim", hex="#FFFFF0"),
        Cor(nome_cor="Neve", hex="#FFFAFA"),
        
        #Vermelho (tudo ok)
        Cor(nome_cor="Serverly burnt toast", hex="#200808"),
        Cor(nome_cor="Red bean", hex="#3F0E04"),
        Cor(nome_cor="Dark sienna", hex="#2F070C"),
        Cor(nome_cor="Rustre red", hex="#410709"),
        Cor(nome_cor="Wine", hex="#4C0004"),
        Cor(nome_cor="Rosewood", hex="#550006"),
        Cor(nome_cor="Cinnabar", hex="#73081A"),
        Cor(nome_cor="Smoked paprika", hex="#571310"),
        Cor(nome_cor="English breakfast", hex="#451616"),
        Cor(nome_cor="Red Cosmos", hex="#632024"),
        Cor(nome_cor="Pantone 763 C", hex="#7C2529"),
        Cor(nome_cor="Pantone 703 C", hex="#9E2A2F"),
        Cor(nome_cor="Pantone 762 C", hex="#8C1D18"),
        Cor(nome_cor="Blood", hex="#5E1104"),
        Cor(nome_cor="Vermelho escuro", hex="#8B0000"),
        Cor(nome_cor="Marrom avermelhado", hex="#800000"),
        Cor(nome_cor="Bloodline", hex="#8B2500"),
        Cor(nome_cor="Christmas", hex="#96291C"),
        Cor(nome_cor="Persian plum", hex="#78201B"),
        Cor(nome_cor="Ruby spice", hex="#A72913"),
        Cor(nome_cor="Mvs Red", hex="#EE0000"),
        Cor(nome_cor="Vermelho", hex="#FF0000"),
        Cor(nome_cor="Firebrick", hex="#CD2626"),
        Cor(nome_cor="Pantone Red C", hex="#F93822"),
        Cor(nome_cor="Chili red", hex="#E13513"),
        Cor(nome_cor="Blood orange", hex="#B50001"),
        Cor(nome_cor="Dark blood red", hex="#CD0000"),
        Cor(nome_cor="Vampire State Building", hex="#CC1400"),
        Cor(nome_cor="Crimson red", hex="#AF1E0B"),
        Cor(nome_cor="Lust", hex="#E4201B"),
        Cor(nome_cor="Strawberry", hex="#A5231C"),
        Cor(nome_cor="Cornell red", hex="#BA1B18"),
        Cor(nome_cor="Tijolo", hex="#B22222"),
        Cor(nome_cor="Pantone 178 C", hex="#FF2D2D"),
        Cor(nome_cor="Pantone 177 C", hex="#FF3B2F"),
        #Laranja (Tudo ok)
        Cor(nome_cor="Chile rojo", hex="#AE431E"),
        Cor(nome_cor="Funky monkey", hex="#B24E1B"),
        Cor(nome_cor="Pleasant pomegranate", hex="#CD3700"),
        Cor(nome_cor="Pantone 172 C", hex="#FA4616"),
        Cor(nome_cor="Pantone 173 C", hex="#CF4520"),
        Cor(nome_cor="Dazzling red", hex="#D9310B"),
        Cor(nome_cor="Vermilion", hex="#E33B08"),
        Cor(nome_cor="Glowing meteor", hex="#EE4000"),
        Cor(nome_cor="Laranja vermelho", hex="#FF4500"),
        Cor(nome_cor="Pantone 724 C", hex="#D45D00"),
        Cor(nome_cor="Pantone 6020 C", hex="#E25800"),
        Cor(nome_cor="Pantone 166 C", hex="#E35205"),
        Cor(nome_cor="Pantone 741 C", hex="#FF6A13"),
        Cor(nome_cor="Pantone 6021 C", hex="#D75A1B"),
        Cor(nome_cor="Pantone 6019 C", hex="#EF6B0D"),
        Cor(nome_cor="Pantone 719 C", hex="#E57200"),
        Cor(nome_cor="Persimmon", hex="#E45B11"),
        Cor(nome_cor="Honey Teriyaki", hex="#F2600C"),
        Cor(nome_cor="Safety medium orange", hex="#FA7301"),
        Cor(nome_cor="Pantone 145 C", hex="#CF7F00"),
        Cor(nome_cor="Pantone 4010 C", hex="#E56910"),
        Cor(nome_cor="Pantone 718 C", hex="#ED8B00"),
        Cor(nome_cor="Pantone 716 C", hex="#FF8200"),
        Cor(nome_cor="Pantone 717 C", hex="#F68D2E"),
        Cor(nome_cor="Pantone 715 C", hex="#EA7600"),
        Cor(nome_cor="Safety orange", hex="#FF7F00"),
        Cor(nome_cor="Laranja escuro", hex="#FF8C00"),
        Cor(nome_cor="Laranja", hex="#FFA500"),
        Cor(nome_cor="Bright yellow", hex="#FFAD33"),
        Cor(nome_cor="Bright orange", hex="#F2AE2E"),
        Cor(nome_cor="Pantone 4008 C", hex="#F4AF23"),
        Cor(nome_cor="Pantone 1575 C", hex="#F7A800"),
        Cor(nome_cor="Pantone 1585 C", hex="#D47F00"),
        Cor(nome_cor="Pantone 2008 C", hex="#F6BE00"),
        Cor(nome_cor="Elden ring orange", hex="#F28B0C"),
        Cor(nome_cor="Chocolate 2", hex="#EE7621"),
        Cor(nome_cor="Chocolate 3", hex="#FF7F24"),
        Cor(nome_cor="Pantone 6018 C", hex="#F58132"),
        Cor(nome_cor="Papaya orange", hex="#E17126"),
        Cor(nome_cor="Orange", hex="#E27921"),
        Cor(nome_cor="Terracota", hex="#D06224"),
        Cor(nome_cor="Pantone 6017 C", hex="#FB914A"),
        Cor(nome_cor="Pantone 4012 C", hex="#EA733D"),
        Cor(nome_cor="Tangerine", hex="#F47729"),
        Cor(nome_cor="Cadmium orange", hex="#F37C34"),
        Cor(nome_cor="Burnt orange", hex="#FE7E3C"),
        Cor(nome_cor="Outrageous Orange", hex="#EB6239"),
        Cor(nome_cor="Rain boots", hex="#FB6734"),
        Cor(nome_cor="Jasper orange", hex="#E48F50"),
        Cor(nome_cor="Pantone 4009 C", hex="#F19C49"),
        Cor(nome_cor="Mimosa", hex="#F7B557"),
        #Marrom (tudo ok)
        Cor(nome_cor="Black bean", hex="#351710"),
        Cor(nome_cor="Chocolate kisses", hex="#45151B"),
        Cor(nome_cor="Garnet", hex="#753130"),
        Cor(nome_cor="Temptren", hex="#44201C"),
        Cor(nome_cor="Persiam plum", hex="#69220F"),
        Cor(nome_cor="Smokey topaz", hex="#862611"),
        Cor(nome_cor="Burnt umber", hex="#7B3221"),
        Cor(nome_cor="Vivid Auburn", hex="#7F3025"),
        Cor(nome_cor="Castanho", hex="#A52A2A"),
        Cor(nome_cor="Marrom 4", hex="#8B2323"),
        Cor(nome_cor="Marrom 3", hex="#CD3333"),
        Cor(nome_cor="Coral 4", hex="#8B3E2F"),
        Cor(nome_cor="Sundried tomato", hex="#7E2A2C"),
        Cor(nome_cor="Tomato 4", hex="#8B3626"),      
        Cor(nome_cor="Brick rust", hex="#7B2A26"),
        Cor(nome_cor="Pantone 4014 C", hex="#B86748"), 
        Cor(nome_cor="Dark chocolate", hex="#443025"),
        Cor(nome_cor="Navajo white 4", hex="#8B795E"),
        Cor(nome_cor="Pantone 736 C", hex="#7A4A2E"),
        Cor(nome_cor="Pantone 1595 C", hex="#9E6A38"),
        Cor(nome_cor="Red panda", hex="#C2441C"),
        Cor(nome_cor="Pantone 167 C", hex="#BE531C"),
        Cor(nome_cor="Aperol", hex="#C1521E"),
        Cor(nome_cor="Garflied", hex="#AA542B"),
        Cor(nome_cor="Pantone 4013 C", hex="#CC6C27"),
        Cor(nome_cor="Chocolate pancakes", hex="#8B4500"),
        Cor(nome_cor="Marrom", hex="#8B4513"),
        Cor(nome_cor="Citrine brown", hex="#A24112"),
        Cor(nome_cor="Siena 1", hex="#A0522D"),
        Cor(nome_cor="Pantone 725 C", hex="#9C4E2A"),
        Cor(nome_cor="Pantone 720 C", hex="#8C4A2F"),
        Cor(nome_cor="Pantone 6027 C", hex="#C3623F"),
        Cor(nome_cor="Pantone 6028 C", hex="#BA5B3F"),
        Cor(nome_cor="Pantone 6026 C", hex="#D57559"),
        Cor(nome_cor="Brown", hex="#AC5840"),
        Cor(nome_cor="Pantone 146 C", hex="#A76D11"),
        Cor(nome_cor="Pantone 139 C", hex="#AF6D04"),
        Cor(nome_cor="Pantone 6007 C", hex="#BC7B28"),
        Cor(nome_cor="Dourado escuro", hex="#B8860B"),
        Cor(nome_cor="Pantone 6006 C", hex="#CF9616"),
        Cor(nome_cor="Pantone 143 C", hex="#F1B434"),
        Cor(nome_cor="Pantone 1245 C", hex="#C69214"),
        Cor(nome_cor="Pantone 160 C", hex="#A1561C"),
        Cor(nome_cor="Pantone 154 C", hex="#9B5A1A"),
        Cor(nome_cor="Pantone 159 C", hex="#CB6015"),
        Cor(nome_cor="Pantone 158 C", hex="#E87722"),
        Cor(nome_cor="Chocolate", hex="#D2691E"),
        Cor(nome_cor="Pantone 153 C", hex="#BE6A14"),
        Cor(nome_cor="Oxide brown", hex="#524033"),
        Cor(nome_cor="Coffee", hex="#6F4D38"),
        Cor(nome_cor="Tawny", hex="#847158"),
        Cor(nome_cor="Aloewood", hex="#7F5836"),
        Cor(nome_cor="Pantone 735 C", hex="#9C6B3E"),
        Cor(nome_cor="Opper", hex="#61413C"),
        Cor(nome_cor="Pantone 6035 C", hex="#945E4B"),
        Cor(nome_cor="Pantone 6034 C", hex="#A06A5A"),
        Cor(nome_cor="Pantone 6033 C", hex="#A97669"),
        Cor(nome_cor="Marrom rosado", hex="#BC8F8F"),
        Cor(nome_cor="Milk tea", hex="#AA7F66"),
        Cor(nome_cor="Pantone 728 C", hex="#C39A6B"),
        Cor(nome_cor="Pantone 733 C", hex="#C19A6B"),
        Cor(nome_cor="Pantone 734 C", hex="#B58150"),
        Cor(nome_cor="Pantone 749 C", hex="#F2E6B2"),
        Cor(nome_cor="Pantone 726 C", hex="#E2C4B9"),
        Cor(nome_cor="Pantone 727 C", hex="#D9B2A9"),
        Cor(nome_cor="Pantone 731 C", hex="#E6C6B3"),
        Cor(nome_cor="Pantone 732 C", hex="#D9B59A"),
        Cor(nome_cor="Smoke tree", hex="#C25F30"),
        Cor(nome_cor="Pantone 4011 C", hex="#DE754C"),
        Cor(nome_cor="Mexican Standoff", hex="#ED9E6F"),
        Cor(nome_cor="Pantone 6016 C", hex="#F49D61"),
        Cor(nome_cor="Pantone 6015 C", hex="#F0B285"),
        Cor(nome_cor="Pantone 150 C", hex="#FFB25B"),
        Cor(nome_cor="Pantone 157 C", hex="#ECA154"),
        Cor(nome_cor="Peru", hex="#CD853F"),
        Cor(nome_cor="Golden yellow", hex="#EDA340"),
        Cor(nome_cor="Chinese bronze", hex="#D28133"),
        Cor(nome_cor="Gold stars", hex="#AF7A2b"),
        Cor(nome_cor="Pantone 750 C", hex="#EED484"),
        Cor(nome_cor="Pantone 751 C", hex="#E5B352"),
        Cor(nome_cor="Pantone 752 C", hex="#CF9F52"),
        Cor(nome_cor="Max yellow red", hex="#EFBC49"),
        Cor(nome_cor="Marrom arenoso", hex="#F4A460"),
        Cor(nome_cor="Tan Brown", hex="#AF7A2B"),
        Cor(nome_cor="Tan", hex="#D1C971"),
        Cor(nome_cor="Caramel", hex="#FBDE9C"),
        Cor(nome_cor="Rubber duchy", hex="#F5E5AB"),
        Cor(nome_cor="Bronzeado", hex="#D2B48C"),
        Cor(nome_cor="Pantone 149 C", hex="#FFC27B"),
        Cor(nome_cor="Burly Wood", hex="#DEB887"),
        
        Cor(nome_cor="Capital yellow", hex="#E3B642"),
        Cor(nome_cor="Moderate yellow", hex="#BFB74B"),
        Cor(nome_cor="Pantone 142 C", hex="#F1BE48"),
        Cor(nome_cor="Pantone 156 C", hex="#F2C75C"),
        Cor(nome_cor="Pantone 1565 C", hex="#F7C46C"),
        #Amarelo (arrumar por cor)
        Cor(nome_cor="Blue yellow", hex="#818807"),
        Cor(nome_cor="Amarelo 4", hex="#8B8B00"),
        Cor(nome_cor="Amarelo 3", hex="#CDCD00"),
        Cor(nome_cor="Goldenrod yellow", hex="#C4C600"),
        Cor(nome_cor="Amarelo 2", hex="#EEEE00"),
        Cor(nome_cor="Amarelo", hex="#FFFF00"),
        Cor(nome_cor="Algae", hex="#AFA231"),
        Cor(nome_cor="Pantone 6005 C", hex="#D9A51B"),
        Cor(nome_cor="Pantone 2007 C", hex="#E0A526"),
        Cor(nome_cor="Pantone 1225 C", hex="#FFC845"),
        Cor(nome_cor="Pantone 1235 C", hex="#FFB81C"),
        Cor(nome_cor="Pantone 7548 C", hex="#FFC600"),
        Cor(nome_cor="Pantone 7549 C", hex="#FFB600"),
        Cor(nome_cor="Pantone 7550 C", hex="#D19000"),
        Cor(nome_cor="Pantone 7551 C", hex="#B47E00"),
        Cor(nome_cor="Pantone 2009 C", hex="#EFB661"),
        Cor(nome_cor="Pantone 2010 C", hex="#FFAD00"),
        Cor(nome_cor="Pantone 2011 C", hex="#ED9B33"),
        Cor(nome_cor="Pantone 2012 C", hex="#EF9600"),
        Cor(nome_cor="Pantone 2013 C", hex="#FF9800"),
        Cor(nome_cor="Pantone 2014 C", hex="#B97000"),
        Cor(nome_cor="Pantone 1355 C", hex="#FFC56E"),
        Cor(nome_cor="Pantone 1365 C", hex="#FFB549"),
        Cor(nome_cor="Pantone 1375 C", hex="#FF9E1B"),
        Cor(nome_cor="Pantone 1395 C", hex="#996017"),
        Cor(nome_cor="Pantone 116 C", hex="#FFCD00"),
        Cor(nome_cor="Pantone 117 C", hex="#C99700"),
        Cor(nome_cor="Pantone 123 C", hex="#FFC72C"),
        Cor(nome_cor="Pantone 124 C", hex="#EAAA00"),
        Cor(nome_cor="Pantone 130 C", hex="#F2A900"),
        Cor(nome_cor="Pantone 131 C", hex="#CC8A00"),
        Cor(nome_cor="Pantone 135 C", hex="#FFC658"),
        Cor(nome_cor="Pantone 136 C", hex="#FFBF3F"),
        Cor(nome_cor="Pantone 137 C", hex="#FFA400"),
        Cor(nome_cor="Pantone 138 C", hex="#DE7C00"),
        Cor(nome_cor="Pantone 378 C", hex="#C6E86B"),
        Cor(nome_cor="Pantone 379 C", hex="#C4E86B"),
        Cor(nome_cor="Pantone 380 C", hex="#CDEA80"),
        Cor(nome_cor="Ouro", hex="#DAA520"),
        Cor(nome_cor="Ouro amarelo", hex="#FFD700"),
        Cor(nome_cor="Amber", hex="#F3B900"),
        Cor(nome_cor="Vivid yellow", hex="#F2BB16"),
        Cor(nome_cor="Glazed apricot", hex="#EAA624"),
        Cor(nome_cor="Xanthous", hex="#F1B12B"),
        Cor(nome_cor="Gold rest", hex="#DF9A3C"),
        Cor(nome_cor="Maize", hex="#FCC74B"),
        Cor(nome_cor="Dark saffron", hex="#EDBF2B"),
        Cor(nome_cor="Saffron", hex="#F8C662"),
        Cor(nome_cor="Light yellow", hex="#DDEC6F"),
        Cor(nome_cor="Moderate yellow", hex="#C8D35F"),
        Cor(nome_cor="Pantone 381 C", hex="#C7EA46"),
        Cor(nome_cor="Pantone 382 C", hex="#BFD730"),
        Cor(nome_cor="Pantone 383 C", hex="#A8AD00"),
        Cor(nome_cor="Pantone 384 C", hex="#949300"),
        Cor(nome_cor="Pantone 385 C", hex="#E9EC6B"),
        Cor(nome_cor="Pantone 386 C", hex="#E3E935"),
        Cor(nome_cor="Pantone 387 C", hex="#E0E721"),
        Cor(nome_cor="Pantone 388 C", hex="#D7DF23"),
        Cor(nome_cor="Pantone 389 C", hex="#CEDC00"),
        Cor(nome_cor="Pantone 390 C", hex="#B2B200"),
        Cor(nome_cor="Pantone 392 C", hex="#F3E500"),
        Cor(nome_cor="Pantone 393 C", hex="#F7EA48"),
        Cor(nome_cor="Pantone 394 C", hex="#EDE939"),
        Cor(nome_cor="Pantone 395 C", hex="#ECE81A"),
        Cor(nome_cor="Pantone 396 C", hex="#F0E900"),
        Cor(nome_cor="Pantone 397 C", hex="#F5E800"),
        Cor(nome_cor="Pantone 398 C", hex="#F4E500"),
        Cor(nome_cor="Pantone 600 C", hex="#F4ED47"),
        Cor(nome_cor="Pantone 601 C", hex="#F5E945"),
        Cor(nome_cor="Pantone 602 C", hex="#FCE300"),
        Cor(nome_cor="Pantone 603 C", hex="#FDDC00"),
        Cor(nome_cor="Pantone 604 C", hex="#F3D03E"),
        Cor(nome_cor="Pantone 605 C", hex="#EEDC00"),
        Cor(nome_cor="Pantone 606 C", hex="#E8D800"),
        Cor(nome_cor="Pantone 607 C", hex="#E1D700"),
        Cor(nome_cor="Pantone 608 C", hex="#E3D900"),
        Cor(nome_cor="Pantone 609 C", hex="#EAE15A"),
        Cor(nome_cor="Pantone 610 C", hex="#F0E99D"),
        Cor(nome_cor="Pantone 611 C", hex="#F1EB9C"),
        Cor(nome_cor="Pantone 612 C", hex="#F6EB61"),
        Cor(nome_cor="Pantone 614 C", hex="#D9D800"),
        Cor(nome_cor="Pantone 615 C", hex="#C5C700"),
        Cor(nome_cor="Cáqui escuro", hex="#BDB76B"),
        Cor(nome_cor="Dourado pálido", hex="#EEE8AA"),
        Cor(nome_cor="Pantone 616 C", hex="#E9E186"),
        Cor(nome_cor="Pantone 617 C", hex="#ECEC8E"),
        Cor(nome_cor="Light grayish yellow", hex="#F2E9CE"),
        Cor(nome_cor="Cáqui", hex="#F0E68C"),
        Cor(nome_cor="Wasabi", hex="#DCD189"),
        Cor(nome_cor="Pantone 618 C", hex="#E6EB8F"),
        Cor(nome_cor="Sunset", hex="#DDEC6f"),
        Cor(nome_cor="Sunset 2", hex="#EAC891"),
        Cor(nome_cor="Pantone 619 C", hex="#E0E27C"),
        Cor(nome_cor="Pantone 620 C", hex="#D0D75C"),
        Cor(nome_cor="Pantone 621 C", hex="#B6BF00"),
        #Verde (tudo ok)
        Cor(nome_cor="Dark green", hex="#0A3323"),
        Cor(nome_cor="Deep olive", hex="#323C31"),
        Cor(nome_cor="Olive moss", hex="#525C44"),
        Cor(nome_cor="hunter green", hex="#41644A"),
        Cor(nome_cor="Pantone 350 C", hex="#234F33"),
        Cor(nome_cor="Pantone 357 C", hex="#215732"),
        Cor(nome_cor="Cadmium Green", hex="#286634"),
        Cor(nome_cor="Pine", hex="#2B5D38"),
        Cor(nome_cor="Deep moss", hex="#3D4421"),
        Cor(nome_cor="Charleston", hex="#1E3309"),
        Cor(nome_cor="Pine tree", hex="#2D3517"),
        Cor(nome_cor="Verde escuro", hex="#006400"),
        Cor(nome_cor="Oliva", hex="#808000"),
        Cor(nome_cor="Dark moss green", hex="#526022"),
        Cor(nome_cor="Elbaete", hex="#535B29"),
        Cor(nome_cor="Old Moss Green", hex="#767B39"),
        Cor(nome_cor="Oliva 2", hex="#8A8635"),
        Cor(nome_cor="Dell", hex="#47632B"),
        Cor(nome_cor="Wicked witch", hex="#66974A"),
        Cor(nome_cor="Overgrowth", hex="#A1AA71"),
        Cor(nome_cor="Moss green", hex="#839958"),
        Cor(nome_cor="Citron", hex="#849A28"),
        Cor(nome_cor="Olive drab 3", hex="#698B22"),
        Cor(nome_cor="Old moss green", hex="#7F8330"),
        Cor(nome_cor="Verde oliva escuro", hex="#556B2F"),
        Cor(nome_cor="Pantone 377 C", hex="#4E5B31"),
        Cor(nome_cor="Pantone 363 C", hex="#4C8C2B"),
        Cor(nome_cor="Pantone 361 C", hex="#43B02A"),
        Cor(nome_cor="Pantone 362 C", hex="#509E2F"),
        Cor(nome_cor="Pantone 353 C", hex="#00B140"),
        Cor(nome_cor="Pantone 354 C", hex="#00A651"),
        Cor(nome_cor="Pantone 355 C", hex="#007A3D"),
        Cor(nome_cor="Pantone 748 C", hex="#009639"),
        Cor(nome_cor="Pantone 360 C", hex="#6CC24A"),
        Cor(nome_cor="Azeitona monótona", hex="#6B8E23"),
        Cor(nome_cor="Chartreuse 4", hex="#458B00"),
        Cor(nome_cor="Verde floresta", hex="#228B22"),
        Cor(nome_cor="Verde", hex="#008000"),
        Cor(nome_cor="Lima", hex="#00FF00"),
        Cor(nome_cor="Verde limão", hex="#32CD32"),
        Cor(nome_cor="Pantone 368 C", hex="#78BE20"),
        Cor(nome_cor="Pantone 375 C", hex="#97D700"),
        Cor(nome_cor="Pantone 376 C", hex="#84BD00"),
        Cor(nome_cor="Chartreuse 3", hex="#66CD00"),
        Cor(nome_cor="Chartreuse 2", hex="#76EE00"),
        Cor(nome_cor="Chartreuse 1", hex="#7FFF00"),
        Cor(nome_cor="Gramado verde", hex="#7CFC00"),
        Cor(nome_cor="Eletric lime", hex="#C6DB00"),
        Cor(nome_cor="Verde amarelo", hex="#ADFF2F"),
        Cor(nome_cor="Amarelo verde", hex="#9ACD32"),
        Cor(nome_cor="Olive drab 2", hex="#B3EE3A"),
        Cor(nome_cor="Citrus", hex="#C4C240"),
        Cor(nome_cor="Olive drab 1", hex="#C0FF3E"),
        Cor(nome_cor="Creme de hortelã", hex="#F5FFFA"),
        Cor(nome_cor="Pantone 358 C", hex="#AEDD7E"),
        Cor(nome_cor="Pantone 359 C", hex="#A1D884"),
        Cor(nome_cor="Pantone 365 C", hex="#C2E189"),
        Cor(nome_cor="Pantone 366 C", hex="#B7DD79"),
        Cor(nome_cor="Pantone 367 C", hex="#A4D65E"),
        Cor(nome_cor="Verde claro", hex="#90EE90"),
        Cor(nome_cor="Verde pálido", hex="#98FB98"),
        Cor(nome_cor="Pantone 351 C", hex="#A7E6A2"),
        Cor(nome_cor="Verde mar", hex="#2E8B57"),
        Cor(nome_cor="Verde mar médio", hex="#3CB371"),
        Cor(nome_cor="Sea green 3", hex="#43CD80"),
        Cor(nome_cor="Verde primavera médio", hex="#00FA9A"),
        Cor(nome_cor="Verde primavera", hex="#00FF7F"),
        Cor(nome_cor="Julip", hex="#5AAA84"),
        Cor(nome_cor="Green trance", hex="#A2D6A1"),
        Cor(nome_cor="Pantone 352 C", hex="#80DFA9"),
        Cor(nome_cor="Verde mar escuro", hex="#8FBC8F"),
        Cor(nome_cor="Pantone 344 C", hex="#A8EBCF"),
        Cor(nome_cor="Pantone 345 C", hex="#91E3C2"),
        #Azul (Tudo ok)
        Cor(nome_cor="Might", hex="#191C20"),
        Cor(nome_cor="Corbeau", hex="#0C111F"),
        Cor(nome_cor="Cetacean blue", hex="#021233"),
        Cor(nome_cor="Trapped Darkness", hex="#0C1D33"),
        Cor(nome_cor="Pantone 276 C", hex="#001E3C"),
        Cor(nome_cor="Blue velvet", hex="#091D38"),
        Cor(nome_cor="Pantone 289 C", hex="#0C2340"),
        Cor(nome_cor="Pantone 275 C", hex="#002A5C"),
        Cor(nome_cor="Dark soul", hex="#0D244D"),
        Cor(nome_cor="Pantone 282 C", hex="#041E42"),
        Cor(nome_cor="Pantone 281 C", hex="#00205B"),
        Cor(nome_cor="Pantone 288 C", hex="#012169"),
        Cor(nome_cor="Pantone 286 C", hex="#0033A0"),
        Cor(nome_cor="Pantone 293 C", hex="#003DA5"),
        Cor(nome_cor="Pantone 294 C", hex="#002F6C"),
        Cor(nome_cor="Pantone 295 C", hex="#002855"),
        Cor(nome_cor="Pantone 303 C", hex="#002A3A"),
        Cor(nome_cor="Black pearl", hex="#1A2C30"),
        Cor(nome_cor="Pantone 309 C", hex="#003B44"),
        Cor(nome_cor="Gunmetal", hex="#2D293B"),
        Cor(nome_cor="Space cadet", hex="#25344F"),
        Cor(nome_cor="Prussian blue", hex="#1B3854"),
        Cor(nome_cor="Pantone 302 C", hex="#003B5C"),
        Cor(nome_cor="Midnight green", hex="#105666"),
        Cor(nome_cor="Pantone 335 C", hex="#007C7A"),
        Cor(nome_cor="Holly", hex="#184F61"),
        Cor(nome_cor="Pantone 329 C", hex="#00685E"),
        Cor(nome_cor="Pantone 328 C", hex="#007367"),
        Cor(nome_cor="Cerceta", hex="#008080"),
        Cor(nome_cor="Dark cyan", hex="#0E6973"),
        Cor(nome_cor="Dark cyan 2", hex="#118C8C"),
        Cor(nome_cor="Pantone 327 C", hex="#008675"),
        Cor(nome_cor="Pantone 322 C", hex="#007377"),
        Cor(nome_cor="Pantone 315 C", hex="#006F71"),
        Cor(nome_cor="Pantone 348 C", hex="#00843D"),
        Cor(nome_cor="Pantone 343 C", hex="#00563F"),
        Cor(nome_cor="Pantone 341 C", hex="#007A53"),
        Cor(nome_cor="Pantone 342 C", hex="#006747"),
        Cor(nome_cor="Pantone 349 C", hex="#006A4D"),
        Cor(nome_cor="Pantone 336 C", hex="#006B5E"),
        Cor(nome_cor="Pantone 340 C", hex="#009E60"),
        Cor(nome_cor="Jungle Green", hex="#0FA27E"),
        Cor(nome_cor="Pantone 314 C", hex="#008996"),
        Cor(nome_cor="Pantone 339 C", hex="#00C389"),
        Cor(nome_cor="Paolo veronese green", hex="#0fA27E"),
        Cor(nome_cor="Aquamarine 4", hex="#458B74"),
        Cor(nome_cor="Pantone 337 C", hex="#9FE2BF"),
        Cor(nome_cor="Pantone 338 C", hex="#6EDBC3"),
        Cor(nome_cor="Pantone 346 C", hex="#71D8AF"),
        Cor(nome_cor="Blue logan", hex="#0E6873"),
        Cor(nome_cor="Pantone 627 C", hex="#007D8A"),
        Cor(nome_cor="Pantone 321 C", hex="#008C95"),
        Cor(nome_cor="Wintergreen dream", hex="#4d8a8b"),
        Cor(nome_cor="Pantone 319 C", hex="#2DCCD3"),
        Cor(nome_cor="Pantone 326 C", hex="#00B2A9"),
        Cor(nome_cor="Dodger blue 4", hex="#104E8B"),
        Cor(nome_cor="Blueberry", hex="#2C3F70"),
        Cor(nome_cor="Azul meia noite", hex="#191970"),
        Cor(nome_cor="Azul marinho", hex="#000080"),
        Cor(nome_cor="Azul escuro", hex="#00008B"),
        Cor(nome_cor="Royal blue 4", hex="#27408B"),
        Cor(nome_cor="Pantone 651 C", hex="#003A8F"),
        Cor(nome_cor="Pantone 650 C", hex="#0067B9"),
        Cor(nome_cor="Azul médio", hex="#0000CD"),
        Cor(nome_cor="Azul 2", hex="#0000EE"),
        Cor(nome_cor="Azul", hex="#0000FF"),
        Cor(nome_cor="Pantone 645 C", hex="#004C97"),
        Cor(nome_cor="Yale blue", hex="#0D3B66"),
        Cor(nome_cor="Pantone 301 C", hex="#004B87"),
        Cor(nome_cor="Pantone 308 C", hex="#00587C"),
        Cor(nome_cor="Blue jeans", hex="#214573"),       
        Cor(nome_cor="Widjammer", hex="#6CA2E8"),
        Cor(nome_cor="Weoldon blue", hex="#729BAE"),
        Cor(nome_cor="Royal blue 1", hex="#4876FF"),
        Cor(nome_cor="Pantone 639 C", hex="#0072CE"),
        Cor(nome_cor="Pantone 638 C", hex="#0085CA"),
        Cor(nome_cor="Pantone 272 C", hex="#307FE2"),
        Cor(nome_cor="Pantone 637 C", hex="#009CDE"),
        Cor(nome_cor="Pantone 299 C", hex="#00A3E0"),
        Cor(nome_cor="Pantone 633 C", hex="#0093A0"),
        Cor(nome_cor="Pantone 632 C", hex="#00A6B2"),
        Cor(nome_cor="Vibrant teal", hex="#00AEC7"),
        Cor(nome_cor="Pantone 298 C", hex="#41B6E6"),
        Cor(nome_cor="Pantone 297 C", hex="#71C5E8"),
        Cor(nome_cor="Azul de aço", hex="#4682B4"),
        Cor(nome_cor="Cadet blue", hex="#5F9EA0"),
        Cor(nome_cor="Cadet blue 5", hex="#53868B"),
        Cor(nome_cor="Starstruck", hex="#4C57A9"),
        Cor(nome_cor="Flor de milho azul", hex="#6495ED"),
        Cor(nome_cor="Azul ardósia", hex="#6A5ACD"),
        Cor(nome_cor="Ardósia média azul", hex="#7B68EE"),
        Cor(nome_cor="Wedgewood", hex="#53728A"),
        Cor(nome_cor="Royal blue 3", hex="#3A5FCD"),
        Cor(nome_cor="Royal blue 2", hex="#436EEE"),
        Cor(nome_cor="Nautica", hex="#487CA2"),
        Cor(nome_cor="Cornflower blue", hex="#608ED8"),
        Cor(nome_cor="Steel Teal", hex="#4D8A8B"),
        Cor(nome_cor="Rackley", hex="#60859e"),
        Cor(nome_cor="Slate blue 3", hex="#6959CD"),
        Cor(nome_cor="Slate blue 2", hex="#7A67EE"),
        Cor(nome_cor="Slate blue 1", hex="#836FFF"),
        Cor(nome_cor="Pantone 654 C", hex="#8CB7E2"),
        Cor(nome_cor="Pantone 655 C", hex="#5E9BD3"),
        Cor(nome_cor="Mar verde claro", hex="#20B2AA"),
        Cor(nome_cor="Pantone 746 C", hex="#00B5E2"),
        Cor(nome_cor="Pantone 747 C", hex="#00A9CE"),
        Cor(nome_cor="Persian green", hex="#13B48F"),
        Cor(nome_cor="Turquesa escuro", hex="#00CED1"),
        Cor(nome_cor="Pantone 311 C", hex="#05C3DE"),
        Cor(nome_cor="Ciano escuro", hex="#008B8B"),
        Cor(nome_cor="Céu azul profundo", hex="#00BFFF"),
        Cor(nome_cor="Pantone 745 C", hex="#5BC2E7"),
        Cor(nome_cor="Ciano 3", hex="#00CDCD"),
        Cor(nome_cor="Ciano 2", hex="#00EEEE"),
        Cor(nome_cor="Ciano", hex="#00FFFF"),
        Cor(nome_cor="Turquesa médio", hex="#48D1CC"),
        Cor(nome_cor="Turquesa", hex="#40E0D0"),
        Cor(nome_cor="Pantone 333 C", hex="#3DB7A4"),
        Cor(nome_cor="Pantone 334 C", hex="#009CA6"),
        Cor(nome_cor="Pantone 279 C", hex="#418FDE"),
        Cor(nome_cor="Dodger blue 3", hex="#1874CD"),
        Cor(nome_cor="Dodger blue 2", hex="#1C86EE"),
        Cor(nome_cor="Dodger blue 1", hex="#1E90FF"),
        Cor(nome_cor="Azul royal", hex="#4169E1"),
        Cor(nome_cor="Cosmic blue", hex="#2288BF"),
        Cor(nome_cor="Pantone 643 C", hex="#3E87CB"),
        Cor(nome_cor="Air Force Blue", hex="#60859E"),
        Cor(nome_cor="Pantone 642 C", hex="#7AA7E1"),
        Cor(nome_cor="Pantone 649 C", hex="#5F9DD6"),
        Cor(nome_cor="Pantone 636 C", hex="#6BB6E8"),
        Cor(nome_cor="Pantone 626 C", hex="#4E9FA6"),
        Cor(nome_cor="Green Sheen", hex="#83B8A2"),
        Cor(nome_cor="Wish", hex="#5BB498"),
        Cor(nome_cor="Pantone 325 C", hex="#5BC2AD"),
        Cor(nome_cor="Pantone 631 C", hex="#4FC3CF"),
        Cor(nome_cor="Pantone 630 C", hex="#77D3E2"),
        Cor(nome_cor="Ciano claro", hex="#E0FFFF"),
        Cor(nome_cor="Pantone 270 C", hex="#BFD7EA"),
        Cor(nome_cor="Turquesa claro", hex="#AFEEEE"),
        Cor(nome_cor="Água marinha", hex="#7FFFD4"),
        Cor(nome_cor="Azul aço claro", hex="#B0C4DE"),
        Cor(nome_cor="Pantone 304 C", hex="#9ADBE8"),
        Cor(nome_cor="Pantone 305 C", hex="#59CBE8"),
        Cor(nome_cor="Pantone 310 C", hex="#6AD1E3"),
        Cor(nome_cor="Aquamarine 2", hex="#76EEC6"),
        Cor(nome_cor="Azul claro", hex="#ADD8E6"),
        Cor(nome_cor="Spindele", hex="#B9CFDD"),
        Cor(nome_cor="Cadet blue 4", hex="#74C5CD"),
        Cor(nome_cor="Cadet blue 3", hex="#8EE5EE"),
        Cor(nome_cor="Cadet blue 2", hex="#98F5FF"),
        Cor(nome_cor="Céu azul", hex="#87CEEB"),
        Cor(nome_cor="Céu azul claro", hex="#87CEFA"),
        Cor(nome_cor="Pó azul", hex="#B0E0E6"),
        Cor(nome_cor="Pantone 271 C", hex="#8FC6E8"),
        Cor(nome_cor="Dark sea green", hex="#83b8a2"),
        Cor(nome_cor="Pantone 628 C", hex="#B8E2E0"),
        Cor(nome_cor="Pantone 629 C", hex="#9ADBDC"),
        Cor(nome_cor="Pantone 634 C", hex="#B1DDEA"),
        Cor(nome_cor="Pantone 635 C", hex="#9AC7E3"),
        Cor(nome_cor="Pantone 622 C", hex="#D6E2E3"),
        Cor(nome_cor="Pantone 623 C", hex="#C1D7D9"),
        Cor(nome_cor="Pantone 624 C", hex="#A6C8CA"),
        Cor(nome_cor="Pantone 625 C", hex="#7FB7BE"),
        Cor(nome_cor="Pantone 640 C", hex="#C7E0F4"),
        Cor(nome_cor="Pantone 641 C", hex="#A7C6ED"),
        Cor(nome_cor="Pantone 646 C", hex="#C8DDF0"),
        Cor(nome_cor="Pantone 647 C", hex="#B7CCE5"),
        Cor(nome_cor="Pantone 648 C", hex="#8DB9E3"),
        Cor(nome_cor="Pantone 324 C", hex="#7AC9B7"),
        Cor(nome_cor="Pantone 332 C", hex="#6EC3B4"),
        Cor(nome_cor="Pantone 318 C", hex="#88DBCE"),
        Cor(nome_cor="Pantone 331 C", hex="#8FD6BD"),
        Cor(nome_cor="Aqua marinho médio", hex="#66CDAA"),
        Cor(nome_cor="Pantone 292 C", hex="#69B3E7"),
        Cor(nome_cor="Pantone 284 C", hex="#6FA7D8"),
        Cor(nome_cor="Pantone 660 C", hex="#6FA1D2"),
        Cor(nome_cor="Pantone 667 C", hex="#6E9ED4"),
        Cor(nome_cor="Pantone 283 C", hex="#92C1E9"),
        Cor(nome_cor="Pantone 317 C", hex="#A7E6D7"),
        Cor(nome_cor="Pantone 278 C", hex="#B4C7E7"),
        Cor(nome_cor="Pantone 652 C", hex="#D6E4F1"),
        Cor(nome_cor="Pantone 653 C", hex="#B9D3EB"),
        Cor(nome_cor="Pantone 277 C", hex="#C4D6E7"),
        Cor(nome_cor="Pantone 316 C", hex="#C6EDE8"), 
        Cor(nome_cor="Pantone 290 C", hex="#B9D9EB"),
        Cor(nome_cor="Pantone 291 C", hex="#9BCBEB"),
        Cor(nome_cor="Pantone 658 C", hex="#CFE3F5"),
        Cor(nome_cor="Pantone 659 C", hex="#A8C7E8"),
        Cor(nome_cor="Pantone 664 C", hex="#E4EBF5"),
        Cor(nome_cor="Pantone 665 C", hex="#C9D8EE"),
        Cor(nome_cor="Pantone 666 C", hex="#A7C3E4"),
        Cor(nome_cor="Light grayish cyan", hex="#BAD9CE"),
        Cor(nome_cor="Azul bebê", hex="#9197AA"),
        Cor(nome_cor="Bright bluebell", hex="#99A5CD"),
        Cor(nome_cor="Van gogh blue", hex="#AADCF2"),
        Cor(nome_cor="Butter cream", hex="#C8D4E5"),
        #Roxo (Tudo ok)
        Cor(nome_cor="Crow", hex="#1C0711"),
        Cor(nome_cor="Aubergine", hex="#26121B"),
        Cor(nome_cor="Dark maroon", hex="#301C1D"),
        Cor(nome_cor="Egg plant", hex="#432033"),
        Cor(nome_cor="Plum purple", hex="#43123F"),
        Cor(nome_cor="Pantone 255 C", hex="#772583"),
        Cor(nome_cor="Magenta escuro", hex="#8B008B"),
        Cor(nome_cor="Magenta 3", hex="#CD00CD"),
        Cor(nome_cor="Magenta 2", hex="#EE00EE"),
        Cor(nome_cor="Pearly purple", hex="#B333AB"),
        Cor(nome_cor="Dark purple", hex="#2C263F"),
        Cor(nome_cor="Claret", hex="#6B1A34"),
        Cor(nome_cor="Pantone 676 C", hex="#7C1F52"),
        Cor(nome_cor="Violeta azul", hex="#8A2BE2"),
        Cor(nome_cor="Violeta escuro", hex="#9400D3"),
        Cor(nome_cor="Pantone 254 C", hex="#981E97"),
        Cor(nome_cor="Deep purple", hex="#6E2585"),
        Cor(nome_cor="Roxo 2", hex="#A020F0"),
        Cor(nome_cor="Cadmium violet", hex="#86299c"),
        Cor(nome_cor="Dark orchid 3", hex="#9A32CD"),
        Cor(nome_cor="Orquídea escura", hex="#9932CC"),
        Cor(nome_cor="Dark orchid 2", hex="#B23AEE"),
        Cor(nome_cor="Dark orchid 1", hex="#BF3EFF"),
        Cor(nome_cor="Pantone 675 C", hex="#9E3D74"),
        Cor(nome_cor="Índigo", hex="#4B0082"),
        Cor(nome_cor="Pantone 262 C", hex="#4A1F6F"),
        Cor(nome_cor="Pantone 261 C", hex="#4E2A84"),
        Cor(nome_cor="Pantone 268 C", hex="#582C83"),
        Cor(nome_cor="Pantone 260 C", hex="#5A2D81"),
        Cor(nome_cor="Pantone 267 C", hex="#5F259F"),
        Cor(nome_cor="Pantone 266 C", hex="#753BBD"),
        Cor(nome_cor="Pantone 259 C", hex="#6E4C9B"),
        Cor(nome_cor="Pantone 258 C", hex="#8C6BB1"),
        Cor(nome_cor="Pantone 265 C", hex="#9063CD"),
        Cor(nome_cor="Slate blue 4", hex="#473C8B"),
        Cor(nome_cor="Midnight orchid", hex="#312A44"),
        Cor(nome_cor="Amerixan purple", hex="#472950"),
        Cor(nome_cor="Japanese violet", hex="#502A50"),
        Cor(nome_cor="Roxo 4", hex="#551A8B"),
        Cor(nome_cor="Roxo 3", hex="#7D26CD"),
        Cor(nome_cor="Dark orchid 4", hex="#68228B"),
        Cor(nome_cor="Slip cove", hex="#7611AD"),
        Cor(nome_cor="Crown Jewel", hex="#512F5C"),
        Cor(nome_cor="Roxo Escuro", hex="#800080"),
        Cor(nome_cor="Ardósia azul escura", hex="#483D8B"),
        Cor(nome_cor="Dark raspberry", hex="#7E2A53"),
        Cor(nome_cor="Amber orange", hex="#7E0950"),
        Cor(nome_cor="French plum", hex="#710755"),
        Cor(nome_cor="Brown coffee", hex="#461D3A"),
        Cor(nome_cor="Tyrian purple", hex="#66023C"),
        Cor(nome_cor="Maroon 4", hex="#8B1C62"),
        Cor(nome_cor="Pantone 242 C", hex="#7C1546"),
        Cor(nome_cor="Deep pink 4", hex="#8B0A50"),
        Cor(nome_cor="Pantone 228 C", hex="#8C1D40"),
        Cor(nome_cor="Pantone 227 C", hex="#B1005D"),
        Cor(nome_cor="Pantone 226 C", hex="#E0007A"),
        Cor(nome_cor="Pantone 220 C", hex="#A50050"),
        Cor(nome_cor="Pantone 221 C", hex="#910048"),
        Cor(nome_cor="Pantone 222 C", hex="#6C1D45"),
        Cor(nome_cor="Pantone 234 C", hex="#A20067"),
        Cor(nome_cor="Pantone 235 C", hex="#840B55"),
        Cor(nome_cor="Pantone 683 C", hex="#8F2A5E"),
        Cor(nome_cor="Pantone 697 C", hex="#8C2D3C"),
        Cor(nome_cor="Pantone 188 C", hex="#76232F"),
        Cor(nome_cor="Pantone 215 C", hex="#9C1A47"),
        Cor(nome_cor="Pantone 219 C", hex="#DA1884"),
        Cor(nome_cor="Magenta", hex="#FF00FF"),
        Cor(nome_cor="Pantone 690 C", hex="#8E2C5B"),
        Cor(nome_cor="Pantone 682 C", hex="#B04A7C"),
        Cor(nome_cor="Pantone 689 C", hex="#B0467C"),
        Cor(nome_cor="Pantone 696 C", hex="#A9445A"),
        Cor(nome_cor="Pantone 695 C", hex="#C25C7C"),
        Cor(nome_cor="Orquídea média", hex="#BA55D3"),
        Cor(nome_cor="Orquídea", hex="#DA70D6"),
        Cor(nome_cor="Violeta", hex="#EE82EE"),
        Cor(nome_cor="Pantone 694 C", hex="#D88DA3"),
        Cor(nome_cor="Pantone 688 C", hex="#C76EA3"),
        Cor(nome_cor="Pantone 680 C", hex="#D995BC"),
        Cor(nome_cor="Pantone 687 C", hex="#D99BC6"),
        Cor(nome_cor="Pantone 681 C", hex="#C76E9E"),
        Cor(nome_cor="Pantone 248 C", hex="#9C4E97"),
        Cor(nome_cor="Pantone 247 C", hex="#BB7EC6"),
        Cor(nome_cor="Pantone 246 C", hex="#CC8AC6"),
        Cor(nome_cor="Pantone 245 C", hex="#E5B2D8"),
        Cor(nome_cor="Ameixa 4", hex="#8B668B"),
        Cor(nome_cor="Chain mail", hex="#827384"),
        Cor(nome_cor="Grape kiss", hex="#80466E"),
        Cor(nome_cor="Tulipan violet", hex="#976D90"),
        Cor(nome_cor="Vivid deep Violet", hex="#86299C"),
        Cor(nome_cor="Vivid violet", hex="#8F4A91"),
        Cor(nome_cor="Crushed rasperry", hex="#AF6384"),
        Cor(nome_cor="Pantone 674 C", hex="#B06C96"),
        Cor(nome_cor="Pantone 673 C", hex="#C98CB3"),
        Cor(nome_cor="Pantone 671 C", hex="#E2C7DF"),
        Cor(nome_cor="Pantone 672 C", hex="#D8B7D4"),       
        Cor(nome_cor="Lilac", hex="#C0A4C4"),
        Cor(nome_cor="Faded violet", hex="#DBBDDC"),
        Cor(nome_cor="Moonraker", hex="#BCB3D8"),
        Cor(nome_cor="Pantone 256 C", hex="#D6BFDD"),
        Cor(nome_cor="Pantone 257 C", hex="#C6AADA"),
        Cor(nome_cor="Pearly purple", hex="#BA71A2"),
        Cor(nome_cor="Pantone 263 C", hex="#D7C6E6"),
        Cor(nome_cor="Pantone 264 C", hex="#C9B5E4"),
        Cor(nome_cor="Medium purple 3", hex="#8968CD"),
        Cor(nome_cor="Medium purple 2", hex="#9F79EE"),
        Cor(nome_cor="Medium purple 1", hex="#AB82FF"),
        Cor(nome_cor="Medium purple 4", hex="#5D478B"),
        Cor(nome_cor="Dusky lilac", hex="#695177"),
        Cor(nome_cor="Ceil", hex="#866F96"),
        Cor(nome_cor="Ultra violet", hex="#595082"),
        Cor(nome_cor="Roxo médio", hex="#9370DB"),
        Cor(nome_cor="Violet", hex="#8089D2"),        
        Cor(nome_cor="Iris mist", hex="#B2B0E1"),
        Cor(nome_cor="Classic rose", hex="#ECD0EC"),
        Cor(nome_cor="Pantone 679 C", hex="#E8B8CE"),
        Cor(nome_cor="Ameixa 3", hex="#CD96CD"),
        Cor(nome_cor="Ameixa 2", hex="#EEAEEE"),
        Cor(nome_cor="Ameixa 1", hex="#FFBBFF"),
        Cor(nome_cor="Ameixa", hex="#DDA0DD"),
        #Rosa (Tudo ok)        
        Cor(nome_cor="Pantone 187 C", hex="#A6192E"),
        Cor(nome_cor="Pantone 200 C", hex="#BA0C2F"),
        Cor(nome_cor="Rosewood", hex="#69021E"),
        Cor(nome_cor="Deep burgundy", hex="#591E27"),
        Cor(nome_cor="Pantone 206 C", hex="#CE0037"),
        Cor(nome_cor="Pantone 207 C", hex="#A50034"),
        Cor(nome_cor="Alabama crimson", hex="#AA0235"),
        Cor(nome_cor="Pantone 743 C", hex="#C8102E"),
        Cor(nome_cor="Pantone 180 C", hex="#BE0F34"),
        Cor(nome_cor="Pantone 199 C", hex="#D50032"),
        Cor(nome_cor="Pantone 185 C", hex="#E4002B"),
        Cor(nome_cor="Pantone 742 C", hex="#E03C31"),
        Cor(nome_cor="Firebrick 3", hex="#EE2C2C"),
        Cor(nome_cor="Firebrick 2", hex="#FF3030"),
        Cor(nome_cor="Pantone 171 C", hex="#FF3F34"),
        Cor(nome_cor="Atomic Tangerine", hex="F99256"),
        Cor(nome_cor="Cinnabar", hex="#EE3B3B"),
        Cor(nome_cor="Coral red", hex="#FF4040"),
        Cor(nome_cor="Carmesim", hex="#DC143C"),
        Cor(nome_cor="Pantone 192 C", hex="#E40046"),
        Cor(nome_cor="Pantone 193 C", hex="#BF0D3E"),
        Cor(nome_cor="Dark deep Cerise", hex="#EC008C"),
        Cor(nome_cor="Deep cerise", hex="#D62987"),
        Cor(nome_cor="Cerise", hex="#E32360"),
        Cor(nome_cor="Flirt", hex="#852E47"),
        Cor(nome_cor="Pantone 744 C", hex="#7D2248"),
        Cor(nome_cor="Pantone 198 C", hex="#DF1995"),
        Cor(nome_cor="Pantone 252 C", hex="#E2007A"),
        Cor(nome_cor="Deep pink 3", hex="#CD1076"),
        Cor(nome_cor="Deep pink 2", hex="#EE1289"),
        Cor(nome_cor="Rosa quente", hex="#FF69B4"),
        Cor(nome_cor="Rosa escuro", hex="#FF1493"),
        Cor(nome_cor="Hot pink eletric", hex="#ec008c"),
        Cor(nome_cor="Hot pink 4", hex="#8B3A62"),
        Cor(nome_cor="Hot pink 3", hex="#CD6090"),
        Cor(nome_cor="Hot pink 2", hex="#EE6AA7"),
        Cor(nome_cor="Hot pink 1", hex="#FF6EB4"),
        Cor(nome_cor="Maroon 3", hex="#CD2990"),
        Cor(nome_cor="Maroon 2", hex="#EE30A7"),
        Cor(nome_cor="Maroon 1", hex="#FF34B3"),
        Cor(nome_cor="Maroon", hex="#B03060"),
        Cor(nome_cor="Pantone 238 C", hex="#E4007C"),
        Cor(nome_cor="Pantone 239 C", hex="#DB3EB1"),
        Cor(nome_cor="Pantone 240 C", hex="#C6007E"),
        Cor(nome_cor="Pantone 241 C", hex="#AF0F7E"),
        Cor(nome_cor="Vermelho violeta médio", hex="#C71585"),
        Cor(nome_cor="Violet red", hex="#D02090"),
        Cor(nome_cor="Pantone 201 C", hex="#9D2235"),
        Cor(nome_cor="Pantone 202 C", hex="#862633"),
        Cor(nome_cor="Pantone 203 C", hex="#8A1538"),
        Cor(nome_cor="Pantone 208 C", hex="#861F41"),
        Cor(nome_cor="Strong pink", hex="#BF2A52"),
        Cor(nome_cor="Pantone 213 C", hex="#E31C79"),
        Cor(nome_cor="Pantone 214 C", hex="#CE0F69"),
        Cor(nome_cor="Pantone 232 C", hex="#E83E8C"),        
        Cor(nome_cor="Madder lake", hex="#CE3737"),
        Cor(nome_cor="Pantone 6049 C", hex="#BB452E"),
        Cor(nome_cor="Pantone 6048 C", hex="#D24F4E"),
        Cor(nome_cor="Pantone 176 C", hex="#FF6F61"),
        Cor(nome_cor="Pantone 6047 C", hex="#D04D46"),
        Cor(nome_cor="Firecracker", hex="#eb6239"),
        Cor(nome_cor="Tomato 3", hex="#CD4E39"),
        Cor(nome_cor="Tomato 2", hex="#EE5C42"),
        Cor(nome_cor="Pantone 170 C", hex="#FF6A5B"),
        Cor(nome_cor="Pantone 165 C", hex="#FF5C39"),
        Cor(nome_cor="Tomate", hex="#FF6347"),
        Cor(nome_cor="Coral 3", hex="#CD5B45"),
        Cor(nome_cor="Coral 2", hex="#EE6A50"),
        Cor(nome_cor="Coral 1", hex="#FF7256"),
        Cor(nome_cor="Coral", hex="#FF7F50"),
        Cor(nome_cor="Peach echo", hex="#F47358"),
        Cor(nome_cor="Vermelho indiano", hex="#CD5C5C"),
        Cor(nome_cor="Bittersweet shimmer", hex="#C74E51"),
        Cor(nome_cor="Pantone 709 C", hex="#B2403E"),
        Cor(nome_cor="Maho gassy", hex="#BF353B"),
        Cor(nome_cor="Soft red", hex="#D96C80"),
        Cor(nome_cor="Froly", hex="#EE666A"),
        Cor(nome_cor="Pomegranate", hex="#C85555"),
        Cor(nome_cor="Citrus gold", hex="#E84F59"),
        Cor(nome_cor="Eternal flame", hex="#A94244"),
        Cor(nome_cor="Cinnamon satin", hex="#D46A79"),
        Cor(nome_cor="Watermelon gelato", hex="#B66570"),
        Cor(nome_cor="Vermelho violeta pálido", hex="#DB7093"),
        Cor(nome_cor="Earthworm", hex="#C07D72"),
        Cor(nome_cor="Young salmon", hex="#FCBEAD"),
        Cor(nome_cor="Air-kiss", hex="#FCDDD2"),
        Cor(nome_cor="Vivid tangerine", hex="#F3A88D"),
        Cor(nome_cor="Pantone 174 C", hex="#FFA38B"),
        Cor(nome_cor="Pantone 175 C", hex="#FF8F7A"),
        Cor(nome_cor="Rosy brown", hex="#D3968C"),
        Cor(nome_cor="Salmão escuro", hex="#E9967A"),
        Cor(nome_cor="Pantone 6025 C", hex="#DC826B"),
        Cor(nome_cor="Pantone 6024 C", hex="#E69684"),
        Cor(nome_cor="Coral claro", hex="#F08080"),
        Cor(nome_cor="Salmão", hex="#FA8072"),
        Cor(nome_cor="Salmão claro", hex="#FFA07A"),
        Cor(nome_cor="Pink 4", hex="#8B636C"),
        Cor(nome_cor="Pink 3", hex="#CD919E"),
        Cor(nome_cor="Pink 2", hex="#EEA9B8"),
        Cor(nome_cor="Pink 1", hex="#FFB5C5"),
        Cor(nome_cor="Pantone 738 C", hex="#F59BBB"),
        Cor(nome_cor="Pantone 183 C", hex="#F65275"),
        Cor(nome_cor="Deep blush", hex="#F2678E"),
        Cor(nome_cor="Pantone 231 C", hex="#E56DB1"),
        Cor(nome_cor="Pantone 197 C", hex="#F04E98"),
        Cor(nome_cor="Pantone 191 C", hex="#EA5276"),
        Cor(nome_cor="Pantone 181 C", hex="#F4B6A7"),
        Cor(nome_cor="Pantone 721 C", hex="#F8C9B8"),
        Cor(nome_cor="Pantone 722 C", hex="#F2A07B"),
        Cor(nome_cor="Pantone 739 C", hex="#EAA794"),
        Cor(nome_cor="Pantone 704 C", hex="#F7DAD9"),
        Cor(nome_cor="Pantone 705 C", hex="#F5C4C2"),
        Cor(nome_cor="Pantone 706 C", hex="#F2A7A3"),
        Cor(nome_cor="Pantone 707 C", hex="#E28482"),
        Cor(nome_cor="Pantone 708 C", hex="#C65D5C"),
        Cor(nome_cor="Pantone 710 C", hex="#FFD6C9"),
        Cor(nome_cor="Pantone 711 C", hex="#FFB3A7"),
        Cor(nome_cor="Pantone 713 C", hex="#FF8674"),
        Cor(nome_cor="Pantone 698 C", hex="#F6D8D8"),
        Cor(nome_cor="Pantone 699 C", hex="#F3C7C6"),
        Cor(nome_cor="Pantone 700 C", hex="#E8A8A6"),
        Cor(nome_cor="Pantone 701 C", hex="#D38D8D"),
        Cor(nome_cor="Pantone 702 C", hex="#B46B6B"),
        Cor(nome_cor="Pantone 162 C", hex="#FFBE9F"),
        Cor(nome_cor="Pantone 163 C", hex="#FF9E7C"),
        Cor(nome_cor="Pantone 168 C", hex="#F0B7A5"),
        Cor(nome_cor="Pantone 169 C", hex="#FF9A8A"),
        Cor(nome_cor="Light coral", hex="#F28983"),
        Cor(nome_cor="Bisque", hex="#FFE4C4"),
        Cor(nome_cor="Amêndoa escaldada", hex="#FFEBCD"),
        Cor(nome_cor="Chiffon de limão", hex="#FFFACD"), 
        Cor(nome_cor="Mocassim", hex="#FFE4B5"),
        Cor(nome_cor="Pantone 155 C", hex="#FADFAA"),
        Cor(nome_cor="Chicote de mamão", hex="#FFEFD5"),
        Cor(nome_cor="Pantone 1555 C", hex="#F9DCA7"),
        Cor(nome_cor="Trigo", hex="#F5DEB3"),
        Cor(nome_cor="Navajo white 2", hex="#EECFA1"),
        Cor(nome_cor="Navajo white", hex="#FFDEAD"),
        Cor(nome_cor="Pale dogwood", hex="#EDBFB2"),
        Cor(nome_cor="Pantone 148 C", hex="#FECB8B"),
        Cor(nome_cor="Flower girl", hex="#F491B4"),
        Cor(nome_cor="Pantone 182 C", hex="#FC9BB3"),
        Cor(nome_cor="Pantone 195 C", hex="#F99FC9"),
        Cor(nome_cor="Pantone 196 C", hex="#F67FB2"),
        Cor(nome_cor="Pantone 209 C", hex="#F2B7C9"),
        Cor(nome_cor="Pantone 211 C", hex="#F57EB6"),
        Cor(nome_cor="Pantone 225 C", hex="#EC86C2"),
        Cor(nome_cor="Pantone 189 C", hex="#F8C9D4"),
        Cor(nome_cor="Pantone 190 C", hex="#F2A2B0"),
        Cor(nome_cor="Pantone 194 C", hex="#F6C1CC"),
        Cor(nome_cor="Pantone 230 C", hex="#F4B8E4"),
        Cor(nome_cor="Pantone 236 C", hex="#F1C6E1"),
        Cor(nome_cor="Pantone 237 C", hex="#EABEDB"),
        Cor(nome_cor="Pantone 204 C", hex="#F1C6CF"),
        Cor(nome_cor="Pantone 205 C", hex="#E6A1B0"),
        Cor(nome_cor="Marvelous", hex="#EA9DAE"),
        Cor(nome_cor="Light pink", hex="#FCA9AA"),
        Cor(nome_cor="Sakura", hex="#EC9C9D"),
        Cor(nome_cor="Plum blossom", hex="#F2A0A1"),
        Cor(nome_cor="Rosa enevoada", hex="#FFE4E1"),
        Cor(nome_cor="Pantone 6023 C", hex="#EAB19E"),
        Cor(nome_cor="Pink opal", hex="#FCD3C5"),
        Cor(nome_cor="Luz rosa", hex="#FFB6C1"),
        Cor(nome_cor="Rosa", hex="#FFC0CB"),
        Cor(nome_cor="Pantone 243 C", hex="#F2D4E6"),
        Cor(nome_cor="Pantone 244 C", hex="#EDCFE5"),
        Cor(nome_cor="Pantone 250 C", hex="#F3CFE3"),
        Cor(nome_cor="Pantone 251 C", hex="#F0A1D1"),
        Cor(nome_cor="Pantone 6022 C", hex="#F5C0B5"),
        Cor(nome_cor="Folha de pêssego", hex="#FFDAB9"),
        Cor(nome_cor="Cor de lavanda", hex="#FFF0F5"),
        Cor(nome_cor="Holographic lavender", hex="#F1E1F5"),
        Cor(nome_cor="Pantone 691 C", hex="#F5DDE2"),
        Cor(nome_cor="Pantone 692 C", hex="#EFCFD6"),
        Cor(nome_cor="Pantone 693 C", hex="#E6B6C1"), 
        Cor(nome_cor="Light melon", hex="#F7BCB0"),
        Cor(nome_cor="Dark apricot", hex="#F6CBB6"),
        Cor(nome_cor="Apricot", hex="#F6CDB6"),
        Cor(nome_cor="Cardo", hex="#D8BFD8"),
        Cor(nome_cor="Pantone 223 C", hex="#F4B8D8"),
        Cor(nome_cor="Pantone 224 C", hex="#F2A1CF"),  
        Cor(nome_cor="Pantone 677 C", hex="#F2DDE6"),
        Cor(nome_cor="Pantone 678 C", hex="#EFD1DC"),
        Cor(nome_cor="Pantone 684 C", hex="#F4E3EB"),
        Cor(nome_cor="Pantone 685 C", hex="#EDD3E2"),
        Cor(nome_cor="Pantone 686 C", hex="#E6BED9"),
        Cor(nome_cor="Pantone 161 C", hex="#F2C3A7"),
        Cor(nome_cor="Champagne pink", hex="#F3D8CE"),
        Cor(nome_cor="Misty rose", hex="#FFF4E1"),     
    ]

    db.session.add_all(cores)
    db.session.commit()
    return "Cores inseridas com sucesso!"


@app.route("/inserir_paletas")
def inserir_paletas():
    
    if Paleta.query.first():
        return "Paletas já existem."
   
    paleta = Paleta(nome_cor_paleta="Palette 8")

    cores = Cor.query.filter(
        Cor.hex.in_([
            "#0C0A03",  
            "#3F0E04",  
            "#A24112",  
            "#47632B",  
            "#Df9A3C",  
        ])
    ).all()

    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Eva citrus palette")

    cores = Cor.query.filter(
        Cor.hex.in_([
            "#D96C80",
            "#BF2A52",
            "#BFB74B",
            "#F2E9CE",
            "#F2AE2E",
        ])
    ).all()

    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Marusya's pink palette")

    cores = Cor.query.filter(
        Cor.hex.in_([
            "#1E3309",
            "#849A28",
            "#E32360",
            "#F2678E",
            "#FCA9AA",
        ])
    ).all()

    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Thais summer lemon Palette")

    cores = Cor.query.filter(
        Cor.hex.in_([
            "#0E6973",
            "#118C8C",
            "#BAD9CE",
	        "#F2BB16",
            "#F8C662",
        ])
    ).all()

    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Gabi's water lily palett")

    cores = Cor.query.filter(
        Cor.hex.in_([
            "#0A3323",
            "#839958",
            "#F7FAD5",
	        "#D3968C",
            "#105666",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Ryna's palette")

    cores = Cor.query.filter(
        Cor.hex.in_([
            "#F8C662",
            "#595082",
            "#2C263F",
	        "#41644A",
            "#0A3323",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Lenee's palette")

    cores = Cor.query.filter(
        Cor.hex.in_([
            "#26121B",
            "#6B1A34",
            "#CE3737",
	        "#FB6734",
            "#1B3854",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Gabrielly's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#AFA231",
            "#4C0004",
            "#DCD189",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Nessie's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#0D3B66",
            "#FFFACD",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Themoi design palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#C4C240",
            "#66023C",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Neutral palette")

    cores = Cor.query.filter(
        Cor.hex.in_([
            "#000000",
            "#FFFFFF",
            "#9CA3AF",
        ])
    ).all()

    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Ditrish's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#0A3323",
            "#C4C240",
            "#E13513",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)
    

    paleta = Paleta(nome_cor_paleta="Red & Beige palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#7B2A26",
            "#525C44",
            "#A39384",
	        "#E4DFD3",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)


    paleta = Paleta(nome_cor_paleta="Senierely's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#FCC74B",
            "#F28983",
            "#E17126",
	        "#C8D35F",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)


    paleta = Paleta(nome_cor_paleta="Palette 3")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#D06224",
            "#AE431E",
            "#8A8635",
	        "#EAC891",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)


    paleta = Paleta(nome_cor_paleta="Olga's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#D1C971",
            "#F3D8CE",
            "#5E1104",
	        "#7F8330",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)


    paleta = Paleta(nome_cor_paleta="Marusya's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#7611AD",
            "#53728A",
            "#B9CFDD",
	        "#CD2626",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)


    paleta = Paleta(nome_cor_paleta="Marusya's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#1E0D0A",
            "#550006",
            "#BF353B",
	        "#EE666A",
            "#3D4421",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Palette 1")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#A72913",
            "#FA8072",
            "#FCD3C5",
            "#E84F59",
            "#571310",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Palette 2")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#DDEC6F",
            "#F3B900",
            "#FA7301",
            "#E45B11",
            "#B50001",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Yana Solomonova's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#BA1B18",
            "#FA8072",
            "#C4C240",
            "#526022",
            "#351710",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Casa chromatica's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#312A44",
            "#695177",
            "#B2B0E1",
            "#F2A0A1",
            "#DAD4D7",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Lux's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#0C1D33",
            "#A94244",
            "#C07D72",
            "#FCBEAD",
            "#FCDDD2",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Marusya's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#2F070C",
            "#410709",
            "#7E1C2E",
	        "#8F4A91",
            "#C25F30",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Casa chromatica cosmic galaxy palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#2288BF",
            "#866F96",
            "#B333AB",
	        "#DDEC6F",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Gelya's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#0C111F",
            "#B66570",
            "#512F5C",
            "#ED9E6F",
            "#80466E",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Elissa's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#43123F",
            "#C4C600",
            "#AF1E0B",
            "#301C1D",
            "#7E0950",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Thais summer tangerine palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#818807",
            "#6CA2E8",
            "#F28B0C",
            "#F2600C",
            "#D9310B",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Cemart bold reds palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#FFAD33",
            "#CC1400",
            "#BCB3D8",
            "#4C57A9",
            "#66974A",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Casa Chromatica's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#852E47",
            "#0D244D",
            "#AA542B",
            "#C2441C",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    

    paleta = Paleta(nome_cor_paleta="Sweet palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#2C3F70",
            "#A5231C",
            "#C8D4E5",
            "#8089D2",
            "#E8EBED",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Duh's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#C5C0AA",
            "#7F3025",
            "#44201C",
            "#4D8A8B",
            "#83B8A2",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)


    paleta = Paleta(nome_cor_paleta="Lenne's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#286634",
            "#F1B12B",
            "#F491B4",
            "#D62987",
            "#86299C",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)


    paleta = Paleta(nome_cor_paleta="Chau's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#E48F50",
            "#753130",
            "#2D293B",
            "#60859E",
            "#729BAE",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)


    paleta = Paleta(nome_cor_paleta="Lenee's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#FFF4E1",
            "#432033",
            "#976D90",
            "#AF6384",
            "#323C31",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)


    paleta = Paleta(nome_cor_paleta="Palette 6")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#A1AA71",
            "#535B29",
            "#847158",
            "#487CA2",
            "#1E0D0A",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)


    paleta = Paleta(nome_cor_paleta="Quetratech's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#11100D",
            "#7B3221",
            "#AC5840",
            "#828D85",
            "#7F858B",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)


    paleta = Paleta(nome_cor_paleta="Quetratech's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#E33B08",
            "#F37C34",
            "#2D3517",
            "#0FA27E",
            "#13B48F",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Palette 7")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#EC008C",
            "#6E2585",
            "#00AEC7",
	        "#C6DB00",
            "#F1E1F5",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Marusya's Palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#96291C",
            "#B7A596",
            "#5BB498",
	        "#184F61",
            "#191C20",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Aespo's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#443025",
            "#7F5836",
            "#AA7F66",
            "#EC9C9D",
            "#FFF4E1",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Lylpert's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#45151B",
            "#EA9DAE",
            "#FBDE9C",
            "#F99256",
            "#C74E51",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)


    paleta = Paleta(nome_cor_paleta="Engie's tomatoes palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#E3B642",
            "#B24E1B",
            "#7E2A2C",
            "#2B5D38",
            "#28171D",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Palette 4")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#AA0235",
            "#69021E",
            "#030206",
            "#021233",
            "#710755",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Tammy van dorn's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#214573",
            "#EDA340",
            "#091D38",
            "#AF7A2B",
            "#F47729",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Sarli murat's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#461D3A",
            "#502A50",
            "#7E2A53",
            "#BA71A2",
            "#ECD0EC",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Glowup's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#A2D6A1",
            "#5AAA84",
            "#591E27",
            "#F5E5AB",
            "#524033",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Palette 5")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#EB6239",
            "#73081A",
            "#1C0711",
            "#827384",
            "#8C7A6C",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Gilded's sunset palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#F47358",
            "#200808",
            "#451616",
            "#DBBDDC",
            "#99A5CD",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Yana Salomonova's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#CD5C5C",
            "#EDBF2B",
            "#608ED8",
            "#808000",
            "#0A3323",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Trevlyn palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#25344F",
            "#708090",
            "#D1C971",
            "#6F4D38",
            "#632024",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Sarli's palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#472950",
            "#C0A4C4",
            "#F6CBB6",
            "#CD3700",
            "#78201B",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Color palette 684")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#69220F",
            "#862611",
            "#D28133",
            "#EFBC49",
            "#F3A88D",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Lenee's blooming palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#C85555",
            "#EAA624",
            "#767B39",
            "#AADCF2",
            "#F7BCB0",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Chris Ann palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#CDD0DB",
            "#9197AA",
            "#F7B557",
            "#E27921",
            "#C1521E",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    paleta = Paleta(nome_cor_paleta="Marusya's inspiration palette")
    cores = Cor.query.filter(
        Cor.hex.in_([
            "#FE7E3C",
            "#E4201B",
            "#61413C",
            "#0E6873",
            "#1A2C30",
        ])
    ).all()
    paleta.cores.extend(cores)
    db.session.add(paleta)

    db.session.commit()
    return "Paletas criadas com sucesso!"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/central_cores')
def central_cores():

    cores_db = Cor.query.all()
    return render_template('central_cores.html', cores=cores_db)

@app.route('/central_paletas')
def central_paletas():
    paletas = Paleta.query.all()
    return render_template("central_paletas.html", paletas=paletas)

if __name__ == '__main__':
    app.run(debug=True)