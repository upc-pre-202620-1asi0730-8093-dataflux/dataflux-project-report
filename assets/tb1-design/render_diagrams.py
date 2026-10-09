"""Render RentBuild design supplements from explicit local data, without changing prior exports.

Run with Python and Pillow from the report root. PNGs are presentation figures;
their matching Mermaid files preserve editable nodes, members and relationships.
They are proposed design, not evidence of deployed software or a team workshop.
"""
from pathlib import Path
import json
import math
import re
import textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
FONT_DIR = Path('C:/Windows/Fonts')
REG = str(FONT_DIR / 'arial.ttf')
BOLD = str(FONT_DIR / 'arialbd.ttf')
MONO = str(FONT_DIR / 'consola.ttf')
INK = '#183449'
COLORS = {'actor':'#edf4fa','system':'#dcecf7','component':'#e9f1f8','command':'#ddecff','event':'#ffe6c8','aggregate':'#fff3c6','query':'#e3f4e4','value':'#f0e9fb','error':'#fde8e7','external':'#f0f0f0'}
INDEX = []

def font(size=28,bold=False,mono=False):
    return ImageFont.truetype(MONO if mono else BOLD if bold else REG,size)

def wrap(draw, value, max_width, f):
    lines=[]
    for raw in str(value).split('\n'):
        words=raw.split(); line=''
        for word in words:
            candidate=(line+' '+word).strip()
            if line and draw.textlength(candidate,font=f)>max_width:
                lines.append(line); line=word
            else: line=candidate
        lines.append(line)
    return lines

def text(draw, xy, value, max_width, size=28, bold=False, mono=False, color=INK):
    f=font(size,bold,mono); x,y=xy
    for line in wrap(draw,value,max_width,f):
        draw.text((x,y),line,font=f,fill=color)
        y+=size+9
    return y

def arrow(draw, points, label='', dashed=False, label_position=None):
    for p,q in zip(points,points[1:]):
        if dashed:
            dx,dy=q[0]-p[0],q[1]-p[1]; distance=math.hypot(dx,dy)
            for at in range(0,int(distance),18):
                end=min(at+10,distance)
                draw.line((p[0]+dx*at/distance,p[1]+dy*at/distance,p[0]+dx*end/distance,p[1]+dy*end/distance),fill='#49677c',width=3)
        else: draw.line((p,q),fill='#49677c',width=3)
    p,q=points[-2:]; angle=math.atan2(q[1]-p[1],q[0]-p[0]); length=15
    draw.polygon([q,(q[0]-length*math.cos(angle-.45),q[1]-length*math.sin(angle-.45)),(q[0]-length*math.cos(angle+.45),q[1]-length*math.sin(angle+.45))],fill='#49677c')
    if label:
        p,q=points[len(points)//2-1:len(points)//2+1]
        x,y=label_position or ((p[0]+q[0])/2,(p[1]+q[1])/2)
        f=font(22); lines=wrap(draw,label,340,f); width=max(draw.textlength(l,font=f) for l in lines)+16; height=len(lines)*29+8
        draw.rectangle((x-width/2,y-height/2,x+width/2,y+height/2),fill='white')
        text(draw,(x-width/2+8,y-height/2+4),'\n'.join(lines),width-16,size=22)

def node(id,title,body,x,y,w=430,h=230,kind='component',image=None):
    return dict(id=id,title=title,body=body,x=x,y=y,w=w,h=h,kind=kind,image=image)

def diagram(name,title,nodes,edges,width=1500,height=1060,note='DESIGN PROPOSAL — NOT DEPLOYMENT EVIDENCE',mmd=None,legend=None,edge_routes=None):
    im=Image.new('RGB',(width,height),'white'); draw=ImageDraw.Draw(im)
    text(draw,(40,28),title,width-80,34,True)
    text(draw,(40,85),note,width-80,22,color='#5a6d7d')
    by_id={n['id']:n for n in nodes}
    for edge_index,(a,b,label,*rest) in enumerate(edges):
        s,t=by_id[a],by_id[b]
        sc=(s['x']+s['w']/2,s['y']+s['h']/2); tc=(t['x']+t['w']/2,t['y']+t['h']/2)
        label_position=None
        if edge_routes and edge_index in edge_routes:
            pts,label_position=edge_routes[edge_index]
        elif name.startswith('userflow-') and edge_index==1:
            # The action-to-decision arrow uses a separate outer lane, keeping
            # its caption clear of the list-to-detail arrow and both mockups.
            start=(s['x']+s['w'],sc[1]); end=(tc[0],t['y'])
            lane=s['y']+s['h']+115
            pts=[start,(width-16,start[1]),(width-16,lane),(end[0],lane),end]
            label_position=((width-16+end[0])/2,lane)
        elif abs(tc[1]-sc[1])<70:
            start=(sc[0],s['y']+s['h']); end=(tc[0],t['y']+t['h']); lane=max(start[1],end[1])+45+(edge_index%2)*12; pts=[start,(start[0],lane),(end[0],lane),end]
        elif abs(tc[0]-sc[0])<70:
            start=(sc[0],s['y']+s['h'] if tc[1]>sc[1] else s['y']); end=(tc[0],t['y'] if tc[1]>sc[1] else t['y']+t['h']); pts=[start,end]
        elif t['x'] >= s['x']+s['w'] or s['x'] >= t['x']+t['w']:
            start=(s['x']+s['w'] if tc[0]>sc[0] else s['x'],sc[1]); end=(t['x'] if tc[0]>sc[0] else t['x']+t['w'],tc[1]); middle=(start[0]+end[0])/2; pts=[start,(middle,start[1]),(middle,end[1]),end]
        else:
            start=(sc[0],s['y']+s['h'] if tc[1]>sc[1] else s['y']); end=(tc[0],t['y'] if tc[1]>sc[1] else t['y']+t['h']); middle=(start[1]+end[1])/2; pts=[start,(start[0],middle),(end[0],middle),end]
        arrow(draw,pts,label,bool(rest and rest[0]),label_position)
    for n in nodes:
        x,y,w,h=n['x'],n['y'],n['w'],n['h']
        draw.rounded_rectangle((x,y,x+w,y+h),radius=12,fill=COLORS.get(n['kind'],COLORS['component']),outline='#698399',width=2)
        if n.get('image'):
            p=ROOT/n['image']; shot=Image.open(p).convert('RGB'); shot.thumbnail((w-20,h-135))
            im.paste(shot,(int(x+(w-shot.width)/2),int(y+70)))
            text(draw,(x+14,y+12),n['title'],w-28,25,True)
            text(draw,(x+14,y+h-54),n['body'],w-28,20)
        else:
            current=text(draw,(x+18,y+14),n['title'],w-36,27,True)
            text(draw,(x+18,current+10),n['body'],w-36,24)
    if legend:
        y=max(n['y']+n['h'] for n in nodes)+100
        for label in legend:
            y=text(draw,(40,y),label,width-80,24)+5
    im.save(OUT/(name+'.png'))
    (OUT/(name+'.json')).write_text(json.dumps({'title':title,'note':note,'nodes':nodes,'edges':edges,'width':width,'height':height},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if mmd is None:
        lines=['flowchart TB']
        for n in nodes:
            label=(n['title']+'<br/>'+n['body']).replace('"',"'").replace('\n','<br/>')
            lines.append(f'  {n["id"]}["{label}"]')
        for a,b,label,*rest in edges:
            connector='-.->' if rest and rest[0] else '-->'
            lines.append(f'  {a} {connector}|"{label}"| {b}')
        mmd='\n'.join(lines)+'\n'
    (OUT/(name+'.mmd')).write_text(mmd,encoding='utf-8')
    INDEX.append({'name':name,'title':title,'note':note})

def class_diagram(name,title,classes,relations):
    cols=2 if len(classes)<=4 else 3
    width=1540 if cols==3 else 1180; bw=440 if cols==3 else 460; gap=(width-80-cols*bw)/(cols-1)
    first_y=210 if name=='uml-subscriptions' else 150
    row_h=590 if name=='uml-subscriptions' else 530
    rows=math.ceil(len(classes)/cols); nodes=[]; lines=['classDiagram']
    for i,(id,label,attrs,methods,kind) in enumerate(classes):
        col,row=i%cols,i//cols
        body='\n'.join(attrs+['──────────']+methods)
        nodes.append(node(id,label,body,40+col*(bw+gap),first_y+row*row_h,bw,410,kind))
        lines.append(f'  class {id} {{')
        if kind=='value': lines.append('    <<valueObject>>')
        if kind=='query': lines.append('    <<interface>>')
        if kind=='event': lines.append('    <<enumeration>>')
        for member in attrs+methods: lines.append('    '+member)
        lines.append('  }')
    edges=[]; legend=[]
    for i,(a,b,relation,label) in enumerate(relations,1):
        lines.append(f'  {a} {relation} {b} : {label}')
        if '<--' in relation:
            edges.append((b,a,f'R{i}'))
        else:
            edges.append((a,b,f'R{i}',relation.startswith('..')))
        kind='composition' if '*--' in relation else 'dependency' if '..>' in relation else 'association'
        direction=f'{b} -> {a}' if '<--' in relation else f'{a} -> {b}'
        legend.append(f'R{i} | {direction} | {kind} | {label}')
    # UML members and cardinalities are preserved verbatim in source, and the
    # relationship labels on the rendered image repeat that cardinality.
    edge_routes=None
    if name=='uml-subscriptions':
        # Each numbered relationship has its own visible caption. R2 uses
        # the clear space above the classes, instead of crossing R1/R3/R4.
        edge_routes={
            0: ([(550,330),(480,330)], (515,330)),
            1: ([(260,210),(260,160),(1280,160),(1280,210)], (770,160)),
            2: ([(700,620),(700,690),(260,690),(260,800)], (500,690)),
            3: ([(840,620),(840,750),(770,750),(770,800)], (840,710)),
            4: ([(1060,1005),(1025,1005),(1025,415),(990,415)], (1025,930)),
        }
    diagram(name,title,nodes,edges,width,190+rows*row_h+len(legend)*72,mmd='\n'.join(lines)+'\n',legend=legend,edge_routes=edge_routes)

def c4():
    diagram('c4-context','RentBuild | C4 Level 1 — System Context',[
        node('operator','Rental Operator','Inventories, rental requests and equipment condition',40,220,410,230,'actor'),
        node('builder','Construction Manager','Searches equipment, requests a period and tracks decisions',40,610,410,230,'actor'),
        node('system','RentBuild','Software system\nRental operations and subscriptions',540,430,440,250,'system'),
        node('external','External service — TBD','Geolocation candidate; vendor and integration not verified',1080,430,380,250,'external'),
    ],[('operator','system','1'),('builder','system','2'),('system','external','Planned integration',True)],height=1020)
    diagram('c4-containers','RentBuild | C4 Level 2 — Target Containers',[
        node('landing','Landing Page','HTML5 / CSS3 / JavaScript\nPublic content and app links',60,180,560,250,'system'),
        node('web','Web Application','Vue / JavaScript\nPrimeVue target + Material Design',880,180,560,250,'system'),
        node('api','RESTful API — planned AV2','ASP.NET Core / C#\nBusiness rules, authorization, OpenAPI',880,580,560,260,'system'),
        node('db','Relational Database — planned','MySQL / EF Core\nOwned tables for six contexts',60,580,560,260,'system'),
    ],[('landing','web','CTA / HTTPS'),('web','api','HTTPS / JSON'),('api','db','EF Core / SQL')],height=1030,note='TARGET: API/DB FUTURE. TB1 FAKE API IS A DEVELOPMENT ADAPTER, NOT THIS API.')
    diagram('c4-components-landing','RentBuild | C4 Level 3 — Landing Container',[
        node('public','Public sections','Value proposition, segments, features and team',50,180),
        node('links','App link adapter','Configured app URL + role-specific registration links',1020,180),
        node('languages','Language resources','English / Latin American Spanish\nBCP47 en-US / es-419\nAliases en_US / es_419',50,630),
        node('footer','Footer and documents','Terms, privacy and accessibility navigation',1020,630),
    ],[('public','links','Routes visitor to app'),('public','languages','Localized content'),('languages','footer','Translated documents')],height=1010)
    diagram('c4-components-web','RentBuild | C4 Level 3 — Vue Web Application',[
        node('views','Presentation','Vue views / Vue Router\nIAM, Profiles, Inventory, Rentals, Maintenance, Subscriptions',50,175,620,270),
        node('stores','Application','Context stores and workflows\nSubscription/session reset and request versions',830,175,620,270),
        node('domain','Domain','Entities / enums / value objects\nMoney and DateRange owned locally',50,635,620,270),
        node('transport','Infrastructure','API adapters / assemblers / FetchClient\nFake API in TB1; real API planned for AV2',830,635,620,270),
    ],[('views','stores','Commands / reactive state'),('stores','domain','Validates local model'),('stores','transport','Requests / responses')],height=1070,note='DESIGN: ALL SIX CONTEXTS. VERIFIED REMOTE SLICE IS IDENTIFIED IN SPRINT 2.')
    diagram('c4-components-api','RentBuild | C4 Level 3 — Future ASP.NET Core API',[
        node('http','HTTP interface','ASP.NET Core controllers\nRequest / response DTOs, validation and OpenAPI',50,175,620,270),
        node('usecases','Application services','IAM, Profiles, Inventory, Rentals, Maintenance, Subscriptions',830,175,620,270),
        node('rules','Domain model','Owned aggregates and invariants\nEvents / repository ports',50,635,620,270),
        node('adapters','Infrastructure adapters','EF Core repositories / MySQL\nExternal service adapter — selection pending',830,635,620,270),
    ],[('http','usecases','Invokes use cases'),('usecases','rules','Applies business rules'),('usecases','adapters','Uses owned ports')],height=1070,note='PROPOSED API — NO BACKEND IMPLEMENTATION OR DEPLOYMENT CLAIM')
    diagram('c4-components-database','RentBuild | C4 Level 3 — Proposed Database Ownership',[
        node('iam','IAM / Profiles','users, company_profiles, provider_profiles\nIdentity and company data',50,200,620,250),
        node('inventory','Inventory','equipment_categories, equipments, availability_blocks\nEquipment, rates and period commitments',830,200,620,250),
        node('rentals','Rentals','rental_requests, rental_contracts, deliveries, equipment_returns',50,640,620,250),
        node('support','Maintenance / Subscriptions','incidents, maintenance_records\nsubscription_plans, user_subscriptions',830,640,620,250),
    ],[('iam','inventory','Referenced by company ID'),('inventory','rentals','Referenced by equipment ID'),('rentals','support','Contract/equipment IDs')],height=1050,note='LOGICAL TABLE GROUPS INSIDE ONE FUTURE MYSQL CONTAINER; NOT MICROSERVICES')

def events():
    diagram('eventstorming-big-picture','RentBuild | Big Picture — Rental Lifecycle',[
        node('equipment','Equipment Registered','Rental operator publishes equipment information',45,190,440,220,'event'),
        node('request','Rental Request Submitted','Construction manager requests dates',535,190,440,220,'event'),
        node('approved','Request Approved / Rejected','Provider decides after checking availability',1025,190,440,220,'event'),
        node('delivery','Equipment Delivered','Approved operation starts using the equipment',1025,625,440,240,'event'),
        node('returned','Equipment Returned','Provider records condition and closes the operation',535,625,440,240,'event'),
        node('maintenance','Maintenance Completed','Only release equipment if no other blocking condition exists',45,625,440,240,'event'),
    ],[('equipment','request','Equipment + period'),('request','approved','Provider decision'),('approved','delivery','Approved only'),('delivery','returned','Return / inspection'),('returned','maintenance','If intervention required')],height=1060,note='DOCUMENTARY RECONSTRUCTION; TEAM WORKSHOP RECORD AND VALIDATION PENDING')
    for name,title,rows in [
        ('eventstorming-core','RentBuild | Design-Level — Core Contexts',[
            ('Inventory','Register / Update Equipment','Equipment','EquipmentRegistered / EquipmentUpdated','Equipment Catalogue + availability'),
            ('Rentals','Submit / Decide Rental Request','RentalRequest / RentalContract','RentalRequestSubmitted / RequestApproved / RequestRejected','Own requests + active contracts'),
            ('Maintenance','Register Incident / Complete Maintenance','Incident / MaintenanceRecord','IncidentRegistered / MaintenanceCompleted','History + blocking maintenance'),
        ]),
        ('eventstorming-support','RentBuild | Design-Level — Supporting Contexts',[
            ('IAM','Register Account / Sign In / Sign Out','User / Session','AccountRegistered / SessionStarted / SessionEnded','Own identity and permissions'),
            ('Profiles','Update Company Profile','CompanyProfile / ProviderProfile','CompanyProfileUpdated','Own profile / public provider'),
            ('Subscriptions','Select / Change Plan','SubscriptionPlan / UserSubscription','DemoPlanSelected / DemoPlanChanged','Plans + current valid period'),
        ])]:
        nodes=[]; edges=[]
        for i,(context,command,aggregate,event,query) in enumerate(rows):
            y=175+i*385
            nodes.extend([node(f'c{i}',context+' | Command',command,40,y,430,240,'command'),node(f'a{i}','Aggregate',aggregate+'\nQuery: '+query,535,y,430,240,'aggregate'),node(f'e{i}','Domain event',event,1030,y,430,240,'event')])
            edges.extend([(f'c{i}',f'a{i}','Validates'),(f'a{i}',f'e{i}','Emits if accepted')])
        diagram(name,title,nodes,edges,height=1380,note='PROPOSED MODEL: COMMAND (BLUE), AGGREGATE (YELLOW), EVENT (ORANGE); NOT IMPLEMENTED BUS')

def classes():
    class_diagram('uml-value-objects','RentBuild | Explicit Value Objects — Future C# Model',[
        ('Money','Money <<value object>>',['- decimal amount','- string currency'],['+ Create(decimal, string) Money','+ Add(Money) Money','+ Equals(Money) bool'],'value'),
        ('DateRange','DateRange <<value object>>',['- DateTime startDate','- DateTime endDate'],['+ Create(DateTime, DateTime)','+ Contains(DateTime) bool','+ Overlaps(DateRange) bool'],'value'),
        ('RentalRate','RentalRate <<value object>>',['- Money amount','- BillingUnit unit'],['+ Create(Money, BillingUnit)','+ Quote(DateRange) Money'],'value'),
        ('Email','Email <<value object>>',['- string value'],['+ Create(string) Email','+ Equals(Email) bool'],'value'),
        ('Address','Address <<value object>>',['- string district','- string city','- string street'],['+ Create(string, string, string)'],'value'),
        ('EquipmentLocation','EquipmentLocation <<value object>>',['- decimal latitude','- decimal longitude','- Address address'],['+ Create(decimal, decimal, Address)'],'value'),
    ],[('RentalRate','Money','"1" *-- "1"','amount 1 : 1'),('EquipmentLocation','Address','"1" *-- "1"','address 1 : 1')])
    class_diagram('uml-iam','RentBuild | IAM — Proposed Domain and Ports',[
        ('User','User <<aggregate>>',['- int id','- Email email','- AccountRole role','- AccountStatus status'],['+ Register(Email, AccountRole)','+ CanAccess() bool'],'aggregate'),
        ('Session','Session',['- int userId','- DateTime expiresAt','- bool revoked'],['+ IsValid(DateTime) bool','+ Revoke() void'],'component'),
        ('AccountRole','AccountRole <<enum>>',['RentalCompany','ConstructionCompany'],[],'event'),
        ('IUserRepository','IUserRepository <<interface>>',[],['+ FindByEmail(Email) User','+ Save(User) void'],'query'),
    ],[('User','Session','"1" --> "0..*"','owns sessions 1 : 0..*'),('User','AccountRole','-->','has role 1 : 1'),('IUserRepository','User','..>','persists users')])
    class_diagram('uml-profiles','RentBuild | Profiles — Proposed Domain and Ports',[
        ('CompanyProfile','CompanyProfile <<aggregate>>',['- int id','- int userId','- string companyName','- Email contactEmail','- Address address'],['+ UpdateContact(Email, Address)'],'aggregate'),
        ('ProviderProfile','ProviderProfile',['- int id','- int companyProfileId','- string publicDescription'],['+ UpdateDescription(string)'],'component'),
        ('Address','Address <<value object>>',['- string street','- string district','- string city'],['+ Create(string, string, string)'],'value'),
        ('IProfileRepository','IProfileRepository <<interface>>',[],['+ FindByUserId(int) CompanyProfile','+ Save(CompanyProfile) void'],'query'),
    ],[('CompanyProfile','ProviderProfile','"1" --> "0..1"','provider view 1 : 0..1'),('CompanyProfile','Address','"1" *-- "1"','address 1 : 1'),('IProfileRepository','CompanyProfile','..>','persists profiles')])
    class_diagram('uml-inventory','RentBuild | Inventory — Proposed Domain and Ports',[
        ('Equipment','Equipment <<aggregate>>',['- int id','- int providerId','- int categoryId','- string serialNumber','- EquipmentStatus status','- RentalRate rate'],['+ UpdateDetails(string)','+ ChangeCondition(EquipmentStatus)'],'aggregate'),
        ('EquipmentCategory','EquipmentCategory',['- int id','- string name'],['+ Rename(string) void'],'component'),
        ('AvailabilityBlock','AvailabilityBlock',['- int id','- int equipmentId','- DateRange period','- string sourceType'],['+ Overlaps(DateRange) bool'],'component'),
        ('EquipmentStatus','EquipmentStatus <<enum>>',['Available','Rented','Maintenance'],[],'event'),
        ('RentalRate','RentalRate <<value object>>',['- Money amount','- BillingUnit unit'],['+ Quote(DateRange) Money'],'value'),
        ('IEquipmentRepository','IEquipmentRepository <<interface>>',[],['+ Find(int) Equipment','+ Save(Equipment) void'],'query'),
    ],[('Equipment','EquipmentCategory','"0..*" --> "1"','category 0..* : 1'),('Equipment','AvailabilityBlock','"1" --> "0..*"','commitments 1 : 0..*'),('Equipment','EquipmentStatus','-->','condition 1 : 1'),('Equipment','RentalRate','"1" *-- "1"','rate 1 : 1'),('IEquipmentRepository','Equipment','..>','persists equipment')])
    class_diagram('uml-rentals','RentBuild | Rentals — Proposed Domain and Ports',[
        ('RentalRequest','RentalRequest <<aggregate>>',['- int id','- int equipmentId','- int requesterId','- int providerId','- DateRange period','- RequestStatus status'],['+ Decide(bool approved)','+ Reject(string reason)'],'aggregate'),
        ('RentalContract','RentalContract <<aggregate>>',['- int id','- int requestId','- Money agreedAmount','- ContractStatus status'],['+ RegisterDelivery(DateTime)','+ RegisterReturn(DateTime)'],'aggregate'),
        ('RequestStatus','RequestStatus <<enum>>',['Pending','Approved','Rejected'],[],'event'),
        ('Delivery','Delivery',['- int id','- int contractId','- DateTime deliveredAt'],['+ Record(DateTime) Delivery'],'component'),
        ('EquipmentReturn','EquipmentReturn',['- int id','- int contractId','- DateTime returnedAt','- string condition'],['+ Record(DateTime, string)'],'component'),
        ('IRentalRepository','IRentalRepository <<interface>>',[],['+ FindRequest(int) RentalRequest','+ SaveContract(RentalContract)'],'query'),
    ],[('RentalRequest','RentalContract','"1" --> "0..1"','accepted request 1 : 0..1'),('RentalRequest','RequestStatus','-->','decision 1 : 1'),('RentalContract','Delivery','"1" --> "0..1"','delivery 1 : 0..1'),('RentalContract','EquipmentReturn','"1" --> "0..1"','return 1 : 0..1'),('IRentalRepository','RentalContract','..>','persists contract')])
    class_diagram('uml-maintenance','RentBuild | Maintenance — Proposed Domain and Ports',[
        ('Incident','Incident <<aggregate>>',['- int id','- int equipmentId','- int? contractId','- string description','- DateTime occurredAt'],['+ Register(string, DateTime)'],'aggregate'),
        ('MaintenanceRecord','MaintenanceRecord <<aggregate>>',['- int id','- int equipmentId','- int? incidentId','- DateRange period','- MaintenanceStatus status'],['+ Schedule(DateRange)','+ Complete() void'],'aggregate'),
        ('MaintenanceStatus','MaintenanceStatus <<enum>>',['Pending','InProgress','Completed'],[],'event'),
        ('IEquipmentConditionPort','IEquipmentConditionPort <<interface>>',[],['+ BlockEquipment(int, DateRange)','+ ReleaseIfUnblocked(int)'],'query'),
    ],[('Incident','MaintenanceRecord','"0..1" --> "0..1"','corrective intervention 0..1 : 0..1'),('MaintenanceRecord','MaintenanceStatus','-->','progress 1 : 1'),('MaintenanceRecord','IEquipmentConditionPort','..>','changes equipment via port')])
    class_diagram('uml-subscriptions','RentBuild | Subscriptions — Proposed Domain and Ports',[
        ('SubscriptionPlan','SubscriptionPlan <<aggregate>>',['- int id','- string name','- Money price','- PlanStatus status'],['+ IsSelectable() bool'],'aggregate'),
        ('UserSubscription','UserSubscription <<aggregate>>',['- int id','- int userId','- int planId','- DateRange period','- SubscriptionStatus status','- bool autoRenew'],['+ IsActive(DateTime) bool','+ ChangePlan(int) void'],'aggregate'),
        ('Money','Money <<value object>>',['- decimal amount','- string currency'],['+ Create(decimal, string) Money'],'value'),
        ('DateRange','DateRange <<value object>>',['- DateTime startDate','- DateTime endDate'],['+ Contains(DateTime) bool'],'value'),
        ('SubscriptionStatus','SubscriptionStatus <<enum>>',['Active','Cancelled','Expired'],[],'event'),
        ('ISubscriptionRepository','ISubscriptionRepository <<interface>>',[],['+ FindCurrent(int) UserSubscription','+ Save(UserSubscription) void'],'query'),
    ],[('SubscriptionPlan','UserSubscription','"1" <-- "0..*"','subscriptions 0..* : 1 selected plan'),('SubscriptionPlan','Money','"1" *-- "1"','price 1 : 1'),('UserSubscription','DateRange','"1" *-- "1"','period 1 : 1'),('UserSubscription','SubscriptionStatus','-->','status 1 : 1'),('ISubscriptionRepository','UserSubscription','..>','persists subscriptions')])
    class_diagram('uml-enumerations','RentBuild | Supporting Enumerations — Future C# Model',[
        ('AccountStatus','AccountStatus <<enum>>',['Active','Disabled'],[],'event'),
        ('ContractStatus','ContractStatus <<enum>>',['Confirmed','Active','Completed'],[],'event'),
        ('PlanStatus','PlanStatus <<enum>>',['Active','Inactive'],[],'event'),
        ('BillingUnit','BillingUnit <<enum>>',['Day','Week','Month'],[],'event'),
    ],[])

def userflows():
    base='assets/md-images-chapter4/web-app-mock_ups/'
    goals=[
        ('inventory','Rental Operator | Register / update equipment','US06–US10',base+'empresa_alquiler/Equipment.png',base+'empresa_alquiler/Equipment.png','Valid required data?','Equipment recorded','Invalid / duplicate: retain input and show reason'),
        ('request','Construction Manager | Find and request equipment','US11–US14',base+'empresa_constructora/Search_equipment.png',base+'empresa_constructora/Equipment _detail.png','Requested period available?','Request PENDING in My Requests','Unavailable / invalid range: choose different dates'),
        ('decision','Rental Operator | Decide a request','US18 / US19',base+'empresa_alquiler/Rental requests.png',base+'empresa_alquiler/Reservations.png','Own pending request? Reject with reason. Approve only if period is available.','APPROVED after availability check, or REJECTED with reason (no availability check).','Other provider / already decided: no change. Unavailable period blocks approval only.'),
        ('rental','Rental Operator | Deliver and record return','US20 / US22',base+'empresa_alquiler/Rentals.png',base+'empresa_alquiler/Rentals.png','Valid contract and preceding step?','Delivery / return recorded once','Missing prior delivery / duplicate: reject operation'),
        ('maintenance','Rental Operator | Record condition and maintenance','US23–US26',base+'empresa_alquiler/Maintenance.png',base+'empresa_alquiler/Equipment.png','Intervention complete + no other blocks?','Equipment released only when fit and unblocked','Incomplete / other blocking work: retain restriction'),
        ('tracking','Construction Manager | Track own request','US21',base+'empresa_constructora/My_requests.png',base+'empresa_constructora/My_requests.png','Own request exists?','Latest PENDING / APPROVED / REJECTED status','Unknown / other company: no private data'),
    ]
    for name,title,ids,img1,img2,condition,success,failure in goals:
        diagram('userflow-'+name,'RentBuild | '+title,[
            node('start','1. Entry / list',ids,40,170,650,460,image=img1),
            node('target','2. Selected action / detail','Prior Figma mockup; states described below',810,170,650,460,image=img2),
            node('condition','3. Decision',condition,40,800,650,220,'query'),
            node('success','4. Expected result',success,810,800,650,220,'event'),
            node('failure','Alternative route',failure,40,1160,650,220,'error'),
        ],[('start','target','Select / inspect'),('target','condition','Submit or query'),('condition','success','Valid / authorized'),('condition','failure','Invalid / unavailable')],height=1530,note='LOGICAL SUPPLEMENT WITH PRIOR MOCKUPS — NOT A NEW FIGJAM EXPORT OR EXECUTION SCREENSHOT')
    diagram('userflow-subscriptions','RentBuild | Rental Operator — Select / Change Plan',[
        node('catalogue','1. Plans','US15: current status and reference plans',40,190,650,245),
        node('confirm','2. Confirmation','US16 / US17: selected plan + demo notice',810,190,650,245),
        node('decision','3. Valid selection?','Active plan exists? Same valid plan is rejected. Expired period may begin a new demo month.',40,620,650,275,'query'),
        node('saved','4. Demo saved','POST new record or PUT current record. Keep valid period; refresh expired period.',810,620,650,275,'event'),
        node('error','Alternative / retry','Load or save error: show translated reason, preserve selection, and retry after reload.',40,1080,650,230,'error'),
    ],[('catalogue','confirm','Select available plan'),('confirm','decision','Confirm once'),('decision','saved','Valid'),('decision','error','Unavailable / failed')],height=1440,note='SUPPLEMENT: PR12 FRONTEND DEMO; NO PAYMENT OR AUTOMATIC BILLING. FORMAL MOCKUP EXPORT PENDING.')

if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    c4(); events(); classes(); userflows()
    (OUT/'index.json').write_text(json.dumps(INDEX,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Rendered {len(INDEX)} PNG design supplements and matching Mermaid/data sources.')
