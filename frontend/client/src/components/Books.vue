<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Books</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Add Book</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Date</th>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{book.date}}</td>
              <td>{{book.title}}</td>
              <td>{{book.author}}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                      type="button"
                      class="btn btn-warning btn-sm"
                      v-b-modal.book-update-modal
                      @click="editBook(book)">
                      Update
                    </button>
                  <button
                      type="button"
                      class="btn btn-danger btn-sm"
                      @click="onDeleteBook(book)">
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addBookModal"
         id="book-modal"
         title="Add a new book"
         hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-date-group"
                    label="Date:"
                    label-for="form-date-input">
          <b-form-input id="form-date-input"
                        type="text"
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addBookForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Author:"
                      label-for="form-author-input">
            <b-form-input id="form-author-input"
                          type="text"
                          v-model="addBookForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editBookModal"
         id="book-update-modal"
         title="Update"
         hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-date-edit-group"
                      label="Date:"
                      label-for="form-date-edit-input">
            <b-form-input id="form-date-edit-input"
                          type="text"
                          v-model="editForm.date"
                          required
                          placeholder="Enter date">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                      label="Author:"
                      label-for="form-author-edit-input">
            <b-form-input id="form-author-edit-input"
                          type="text"
                          v-model="editForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      books: [],
      addBookForm: {
        date: '',
        title: '',
        author: '',
      },
      editForm: {
        id: '',
        date: '',
        title: '',
        author: '',
      },
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:8000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
            console.error(error);
        });
    },
    addBook(payload) {
      const path = 'http://localhost:8000/books';
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book added!';
          this.showMessage = true;
        })
        .catch(() => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:8000/books/${bookID}`;
      axios.put(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    removeBook(bookID) {
      const path = `http://localhost:8000/books/${bookID}`;
      axios.delete(path)
        .then(() => {
          this.getBooks();
          this.message = 'Book removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    onDeleteBook(book) {
      this.removeBook(book.id);
    },
    editBook(book) {
      this.editForm = book;
    },
    initForm() {
      this.addBookForm.date = '';
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.editForm.id = '';
      this.editForm.date = '';
      this.editForm.title = '';
      this.editForm.author = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      const payload = {
        date: this.addBookForm.date,
        title: this.addBookForm.title,
        author: this.addBookForm.author,
      };
      this.addBook(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      const payload = {
        date: this.editForm.date,
        title: this.editForm.title,
        author: this.editForm.author,
      };
      this.updateBook(payload, this.editForm.id);
    },
    OnResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      this.initForm();
      this.getBooks();
    },
    OnReset(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
