<template>
    <HomeSlot>
        <mu-row gutter>
            <mu-col span="6" class="users-list">
                <mu-button @click="addUser" class='style_btn'>Создать пользователя</mu-button>
                <div >
					
						<table border="1" width="100%" cellspacing="0" >
							<tr > 
							
								<th>Имя</th>
								<th>Фамилия</th>
								<th>Отчетсво</th>
								<th>тел.</th>
						   </tr>
						   <tbody v-for="userlen in users">
						   <tr v-for="user in userlen"  @click="openUser(user)"> 
							
							<th >{{user.first_name}}</th>
							<th>{{user.full_name}}</th>
							<th>{{user.patronymic}}</th>
							<th>{{user.telefon}}</th>
						   </tr>
						   </tbody>
						 </table>
					
                </div>
				
				  <button @click="addItem()" class='style_btn'>продолжить</button>
            </mu-col>
			
			<mu-col span="6" class="users-list">
					<div v-if="root==1">Выберите пользователя</div>
					<div v-else-if="root==2">
						<h3>Создать пользователя</h3>
						<input v-model="createForm.first_name" name="your-name" value="" id='user_name' placeholder="Имя *" size="20" type="text">
						<input v-model="createForm.full_name" name="your-name" value="" id='user_name' placeholder="Фамилия *" size="20" type="text">
						<input v-model="createForm.patronymic" name="your-name" value="" id='user_patr' placeholder="Отчетсво" size="20" type="text">
						<input v-model="createForm.telefon" name="your-subject" value="" placeholder="Телефон *" size="20">
						
						<mu-button class="btn-send style_btn" round color="success" @click="CreateUser">Создать пользователя</mu-button>
					</div>
					<div v-else>
						<h3>Пользователь {{form.first_name}}</h3>
						<input v-model="form.first_name" name="your-name" value="" id='user_name' placeholder="Имя *" size="20" type="text">
						<input v-model="form.full_name" name="your-name" value="" id='user_name' placeholder="Фамилия *" size="20" type="text">
						<input v-model="form.patronymic" name="your-name" value="" id='user_patr' placeholder="Отчетсво" size="20" type="text">
						<input v-model="form.telefon" name="your-subject" value="" placeholder="Телефон *" size="20">
						
						
						<mu-button class="btn-send style_btn" round color="success" @click="editUser">Редактировать</mu-button>
						<mu-button class="btn-send style_btn" round color="success" @click="delUser">Удалить</mu-button>
						
					</div>
						
            </mu-col>
			

        </mu-row>
    </HomeSlot>
</template>

<script>
    import HomeSlot from '../Home'

    export default {
        name: "User",
        components: {
            HomeSlot,
        },
        data() {
            return {
                users: [],
				root: '1',
				form: {
					id:'',
                    first_name: '',
					full_name: '',
					patronymic: '',
					telefon: ''
                },
				createForm: {
                    first_name: '',
					full_name: '',
					patronymic: '',
					telefon: ''
                },
            } 

        },
        created() {
            this.loaduser()
        },
        methods: {
			addItem(){
			// Добавить пользователей
				$.ajax({
                    url: "http://127.0.0.1:8000/api/v1/users/user/",
                    type: "GET",
					data: {						
                        userlast: this.users[this.users.length - 1][this.users[this.users.length - 1].length-1].id,
                    },
                    success: (response) => {
                        this.users.push(response.data.data)
						console.log(this.users)
                    }
                })
			},
            // Загружаю список пользователей
            loaduser() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/users/user/",
                    type: "GET",
					data: {						
                        userlast: 'load',
                    },
                    success: (response) => {
                        this.users.push(response.data.data) // this.users = response.data.data
						console.log(this.users)
                    }
                })
            },
            openUser(id) {
				// Открыть карту пользователя
				this.root=3
				for (var key in id) {
					  this.form[key] = id[key];
					}
				
            },
			editUser() {
				// Редактирование пользователя
				
				if (!this.form.first_name) {alert("Поле имя должно быть заполнено");}
				if (!this.form.full_name) {alert("Поле фамилия должно быть заполнено");}
				if (!this.form.telefon) {alert("Поле телефон должно быть заполнено");}
				else {
					var new_tel = this.form.telefon.replace(/\s|\-|\(|\)/g, '');
					var par_pattern = /^\d[\d\(\)\ -]{4,15}\d$/;
					var pro = par_pattern.test(new_tel);
					if ( pro==false) { alert("Телефон должен быть от 4 до 15 символов и без букв!")} else {this.form.telefon=new_tel}
				}
				
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/users/user/",
                    type: "PATCH",
                    data: this.form,
                    success: (response) => {
                        
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                }) 
            },
			
			
            // Создание пользователя
			
            addUser() {
				this.root=2
            },
			CreateUser() {
			
				if (!this.createForm.first_name) {alert("Поле имя должно быть заполнено");}
				if (!this.createForm.full_name) {alert("Поле фамилия должно быть заполнено");}
				if (!this.createForm.telefon) {alert("Поле телефон должно быть заполнено");}
				else {
					var new_tel = this.createForm.telefon.replace(/\s|\-|\(|\)/g, '');
					var par_pattern = /^\d[\d\(\)\ -]{4,15}\d$/;
					var pro = par_pattern.test(new_tel);
					if ( pro==false) { alert("Телефон должен быть от 4 до 15 символов и без букв!")} else {this.createForm.telefon=new_tel}
				}
				
				$.ajax({
                    url: "http://127.0.0.1:8000/api/v1/users/user/",
                    type: "POST",
                    data: this.createForm,
                    success: (response) => {
                        alert('Пользователь добавлен.')
                    },
                    error: (response) => {
                        alert('Ошибка формы. Телефон не уникален.')
                    }
                }) 
			},
			
			// Удаление пользователя
            delUser() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/users/user/",
                    type: "DELETE",
					data: this.form,
                    success: (response) => {
                        alert('Пользователь удален.')
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            }
        }
    }
</script>

<style scoped>
    tr {
        cursor: pointer;
    }

    .users-list {
        box-shadow: 1px 4px 5px #848181;
    }
	input {
	clear: both; 
	display: block;
	margin: 10px auto;
	}
	.style_btn{
	margin: 10px;
	}
</style>
