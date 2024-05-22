create table  Product (
ProductId int identity(1,1) primary key not null,
Barcode numeric	(13) not null,
SKUNumber varchar (20) not null,
ProductName varchar (100) not null,
ProductPrice money not null,
CategoryId int not null,
CollectionId int not null,
ProductColorId int not null,
ProductSizeId int not null,
SeasonId char not null,
FabricTechId char not null,
TypeId int not null,
UnitsinStock int not null,

foreign key (CategoryId) references Category(CategoryId),
foreign key (CollectionId) references [Collection](CollectionId),
foreign key (ProductColorId) references ProductColor(ProductColorID),
foreign key (ProductSizeId) references ProductSize(ProductSizeId),

);

create table Category(
CategoryId int not null,
CategoryName varchar (25) not null,

primary key (CategoryId),

);

create table [Collection](
CollectionId int not null,
CollectionName varchar (20)not null,

primary key (CollectionId),
);

create table ProductColor(
ProductColorId int not null,
ProductColorName varchar (15)not null,

primary key (ProductColorId),
);

create table ProductSize(
ProductSizeId int not null,
ProductSizeName varchar (10)not null,

primary key (ProductSizeId),
);

create table Customer (
CustomerID int NOT NULL, 
CustomerName varchar(15) NOT NULL, 
[Address] varchar(50) NOT NULL, 
Phone varchar not null,
Country varchar (20) not null,
City varchar (20) not null,

primary key (CustomerId) 
); 

create table [Order](
OrderId int not null,
CustomerId int not null,
RequiredDate date,
ShippedDate date,
Freight money,
OrderDate date not null,


foreign key (CustomerId) references Customer(CustomerID),
);

create table [Type](
TypeId int not null,
TypeName varchar (20) not null,
TypeCode char (2) not null,

primary key (TypeId),
);

create table OrderDetails (
OrderId int,
ProductId int,
)

drop table OrderDetails

CREATE TABLE OrderProducts (
  ProductId INT NOT NULL,
  OrderId INT NOT NULL,
  UnitPrice DECIMAL(10,2) NOT NULL,
  Quantity INT NOT NULL,
  PRIMARY KEY (ProductId, OrderId),
  FOREIGN KEY (ProductId) REFERENC0ES Product(ProductId),
  FOREIGN KEY (OrderId) REFERENCES [Order](OrderId)
);

alter table [Order] add primary key (OrderId);

alter table Product add foreign key (TypeId) references [Type](TypeId);

alter table Product add Gender char;

select USER_NAME(1)

alter table ProductColor alter column ProductColorName varchar (50)

select * from [Type]